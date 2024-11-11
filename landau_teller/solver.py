import numpy as np
from numbers import Number
from scipy.integrate import odeint
from scipy.optimize import fsolve
from .constants import kb

class Solution:
    def __init__(self):
        self.energies = None
        self.temperatures = None
        self.time = None

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
            evib[i] = gas.vibmodes[i].degen * kb * frac / (np.exp(frac) - 1.0) * temp
        elif len(temp) == len(gas.vibmodes):
            frac = gas.vibmodes[i].theta/temp[i]
            evib[i] = gas.vibmodes[i].degen * kb * frac / (np.exp(frac) - 1.0) * temp[i]
        elif len(temp) == 1:
            frac = gas.vibmodes[i].theta/temp[0]
            evib[i] = gas.vibmodes[i].degen * kb * frac / (np.exp(frac) - 1.0) * temp[0]
        else:
            raise Exception("wrong format", temp)

    return evib

def calc_dedt(y, t, gas, etot, nrho, rotrelax, vibrelax):
    ekin = etot - sum(y)
    temp = ekin / (1.5 * kb)
    nu = calc_coll_freq(gas, nrho, temp)
    erot_eq = calc_erot(gas, temp) if rotrelax else 0.0
    evib_eq = calc_evib(gas, temp) if vibrelax else [0.0]
    dedt = np.zeros(len(y))

    dedt[0] = nu * (erot_eq - y[0]) / gas.Zrot

    for i in range(len(evib_eq)):
        dedt[i + 1] = nu * (evib_eq[i] - y[i + 1]) / gas.vibmodes[i].Z

    return dedt

def calc_energies(sol, etot):
    shape = (sol.shape[0], sol.shape[1] + 1)
    energies = np.zeros(shape)

    for i in range(len(energies)):
        energies[i][0] = etot

        for k in range(1, shape[1]):
            energies[i][0] -= sol[i][k - 1]
            energies[i][k] = sol[i][k - 1]

    return energies

def eqn2solve(temps, evibs, gas):
    return calc_evib(gas, temps) - evibs

def calc_temperatures(energies, gas):
    temperatures = np.zeros(energies.shape)

    for i in range(len(energies)):
        temperatures[i][0] = energies[i][0] / (1.5 * kb)
        temperatures[i][1] = energies[i][1] / (0.5 * gas.dof_rot* kb)

        evibs = np.array([energies[i][k] for k in range(2, energies.shape[1])])
        guess = np.ones(evibs.size)*300.0
        vibtemps = fsolve(eqn2solve, guess, args=(evibs, gas))

        for k in range(vibtemps.size):
            temperatures[i][k + 2] = vibtemps[k]

    return temperatures

def solve(gas, nrho, temp, trot, tvib, t, **kwargs):
    rotrelax = kwargs["rotrelax"] if "rotrelax" in kwargs else True
    vibrelax = kwargs["vibrelax"] if "vibrelax" in kwargs else True
    ekin0 = calc_ekin(gas, temp)
    erot0 = calc_erot(gas, trot) if rotrelax else 0.0
    evib0 = calc_evib(gas, tvib) if vibrelax else [0.0]
    etot = ekin0 + erot0 + sum(evib0)
    y0 = np.concatenate(([erot0], evib0))
    sol = [y0]

    for _ in range(len(t) - 1):
        dedt = calc_dedt(sol[-1], t, gas, etot, nrho, rotrelax, vibrelax)
        res = sol[-1] + dedt*t[1]
        sol.append(res)

    sol = np.array(sol)
    solution = Solution()

    solution.energies = calc_energies(sol, etot)
    solution.temperatures = calc_temperatures(solution.energies, gas)
    solution.time = t

    return solution

def calc_etot(temp, gas, etot0, rotrelax, vibrelax):
    ekin = calc_ekin(gas, temp)
    erot = calc_erot(gas, temp) if rotrelax else 0.0
    evib = sum(calc_evib(gas, temp)) if vibrelax else 0.0

    return ekin + erot + evib - etot0

def calc_temp_eq(gas, temp, trot, tvib, **kwargs):
    rotrelax = kwargs["rotrelax"] if "rotrelax" in kwargs else True
    vibrelax = kwargs["vibrelax"] if "vibrelax" in kwargs else True
    ekin0 = calc_ekin(gas, temp)
    erot0 = calc_erot(gas, trot) if rotrelax else 0.0
    evib0 = sum(calc_evib(gas, tvib)) if vibrelax else 0.0

    etot0 = ekin0 + erot0 + evib0

    return fsolve(calc_etot, temp, args=(gas, etot0, rotrelax, vibrelax))