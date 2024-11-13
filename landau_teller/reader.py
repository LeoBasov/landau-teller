import json
from .gas import Gas, Vibmode
import numpy as np

def read_output(file_name):
    names = []
    data = {}

    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            splt = line.split(',')

            if len(names) == 0:
                for name in splt:
                    names.append(name)
                    data[name] = []
            else:
                for i in range(len(splt)):
                    data[names[i]].append(float(splt[i]))

    for key, value in data.items():
        data[key] = np.array(value)

    return data

def read_species(file_name):
    gas = Gas()

    with open(file_name) as f:
        data = json.load(f)

        gas.name = data["name"]
        gas.mass = data["mass"]

        gas.vhs.dref = data["vhs"]["dref"]
        gas.vhs.Tref = data["vhs"]["Tref"]
        gas.vhs.omega = data["vhs"]["omega"]
        gas.vhs.alpha = data["vhs"]["alpha"]
        gas.vhs.Zrotinf = data["vhs"]["Zrotinf"]
        gas.vhs.Tstar = data["vhs"]["T*"]
        gas.vhs.C1 = data["vhs"]["C1"]
        gas.vhs.C2 = data["vhs"]["C2"]

        gas.dof_rot = data["rotation"]["dof"]
        gas.Zrot = data["rotation"]["Z"]

        gas.dof_vib = data["vibration"]["dof"]

        for mode in data["vibration"]["modes"]:
            vibmode = Vibmode()

            vibmode.theta = mode["theta"]
            vibmode.degen = mode["degen"]
            vibmode.Z = mode["Z"]

            gas.vibmodes.append(vibmode)

    return gas