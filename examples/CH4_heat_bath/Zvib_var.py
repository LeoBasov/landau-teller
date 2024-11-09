import landau_teller as lt
import matplotlib.pyplot as plt
import numpy as np

file_name = "data/CH4.json"
co2 = lt.read_species(file_name)
temp = 10000.0
trot = 7500.0
tvib = 5000.0
nrho = 2e22
t = np.linspace(0, 1e-5, 1000)

co2.Zrot = 10
co2.Zvib = [20,30, 40, 50]

sol = lt.solve(co2, nrho, temp, trot, tvib, t)

plt.plot(sol.time, sol.temperatures)
plt.show()

lt.write_solution(sol, "CH4", "csv")

print("done")