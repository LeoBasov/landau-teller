import numpy as np
from numbers import Number
from .constants import kb

def calc_coll_freq(gas, nrho, temp):
    return 4.0 * gas.vhs.dref**2 * nrho * np.sqrt(np.pi * kb * gas.vhs.Tref / gas.mass) * (temp/gas.vhs.Tref)**(1.0 - gas.vhs.omega)

def calc_ekin(gas, temp):
    return 1.5 * kb * temp

def calc_erot(gas, temp):
    return 0.5 * gas.dof_rot * kb * temp

def calc_evib(gas, temp):
    evib = np.zeros(len(gas.vibmodes))

    for i in range(len(evib)):
        if isinstance(temp, Number):
            frac = gas.vibmodes[i].theta/temp
            evib[i] = gas.vibmodes[i].degen * 0.5 * kb * frac / (np.exp(frac) - 1.0) * temp
        elif len(temp) == len(gas.vibmodes):
            frac = gas.vibmodes[i].theta/temp[i]
            evib[i] = gas.vibmodes[i].degen * 0.5 * kb * frac / (np.exp(frac) - 1.0) * temp[i]
        else:
            raise Exception("wrong format")

    return evib