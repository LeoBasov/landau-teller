import unittest
import sys

sys.path.append('.')

import landau_teller.solver as so
import landau_teller.reader as rd

class TestSolver(unittest.TestCase):
    def test_read_calc_coll_freq(self):
        file_name = "data/CO2.json"
        co2 = rd.read_species(file_name)
        nrho = 1e20
        temp = 300

        nu = so.calc_coll_freq(co2, nrho, temp)

        self.assertEqual(1.9299072751158094e-05, 1/nu)

    def test_calc_evib(self):
        file_name = "data/CO2.json"
        co2 = rd.read_species(file_name)
        temp = 300
        temps = [300, 400, 500]

        evibs1 = so.calc_evib(co2, temp)
        evibs2 = so.calc_evib(co2, temps)

        self.assertEqual(evibs1[0], evibs2[0])

    def test_solve(self):
        file_name = "data/CO2.json"
        co2 = rd.read_species(file_name)
        temp = 300
        trot = 400
        tvib = 500