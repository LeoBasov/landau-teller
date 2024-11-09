import numpy as np
from .constants import kb

def calc_coll_freq(gas, nrho, temp):
    return 4.0 * gas.vhs.dref**2 * nrho * np.sqrt(np.pi * kb * gas.vhs.Tref / gas.mass) * (temp/gas.vhs.Tref)**(1.0 - gas.vhs.omega)