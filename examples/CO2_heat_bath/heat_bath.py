import landau_teller as lt
import matplotlib.pyplot as plt
import numpy as np

file_name = "data/CO2.json"
co2 = lt.read_species(file_name)
temp = 10000.0
trot = 7500.0
tvib = 5000.0
nrho = 2e22
t = np.linspace(0, 1e-5, 100)

co2.Zrot = 10

for vibmode in co2.vibmodes:
    vibmode.Z = 50

sol = lt.solve(co2, nrho, temp, trot, tvib, t)

plt.plot(sol.time, sol.temperatures)
plt.show()

lt.write_solution(sol, "solution", "csv")

print("done")