import landau_teller as lt
import matplotlib.pyplot as plt
import numpy as np

file_name = "data/N2.json"
N2 = lt.read_species(file_name)
temp = 10000.0
trot = 7500.0
tvib = 5000.0
nrho = 2e22
t = np.linspace(0, 0.25e-5, 100)

N2.Zrot = 10
N2.Zvib = 25

sol = lt.solve(N2, nrho, temp, trot, tvib, t, vibrelax=False)
temp_eq = np.ones(sol.time.size) * lt.calc_temp_eq(N2, temp, trot, tvib, vibrelax=False)

plt.plot(sol.time, sol.temperatures[:,0])
plt.plot(sol.time, sol.temperatures[:,1])
plt.plot(sol.time, temp_eq, "--")
plt.show()

lt.write_solution(sol, "N2", "csv")

print("done")