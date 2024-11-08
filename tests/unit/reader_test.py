import unittest
import sys

sys.path.append('.')

import landau_teller.reader as rd

class TestReader(unittest.TestCase):
    def test_read_species(self):
        file_name = "data/CO2.json"
        co2 = rd.read_species(file_name)

        self.assertEqual("CO2", co2.name)
        self.assertEqual(7.31e-26, co2.mass)

        self.assertEqual(2, co2.dof_rot)
        self.assertEqual(4, co2.dof_vib)
        self.assertEqual(5, co2.Zrot)

        self.assertEqual(5.62e-10, co2.vhs.dref)
        self.assertEqual(273, co2.vhs.Tref)
        self.assertEqual(0.8, co2.vhs.omega)
        self.assertEqual(1, co2.vhs.alpha)
        self.assertEqual(18.1, co2.vhs.Zrotinf)
        self.assertEqual(91.5, co2.vhs.Tstar)
        self.assertEqual(25.48, co2.vhs.C1)
        self.assertEqual(177.98, co2.vhs.C2)

        self.assertEqual(20, co2.vibmodes[0].Z)
        self.assertEqual(1918.6, co2.vibmodes[0].theta)
        self.assertEqual(1, co2.vibmodes[0].degen)

        self.assertEqual(20, co2.vibmodes[1].Z)
        self.assertEqual(3382.0, co2.vibmodes[1].theta)
        self.assertEqual(1, co2.vibmodes[1].degen)

        self.assertEqual(20, co2.vibmodes[2].Z)
        self.assertEqual(959.0, co2.vibmodes[2].theta)
        self.assertEqual(2, co2.vibmodes[2].degen)