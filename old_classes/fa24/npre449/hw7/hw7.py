import numpy as np
import matplotlib.pyplot as plt

# question 2
r2 = np.linspace(0, 1, 1000)

def norm_temp2(r): return r**4 / 3 - 4 * r**2 / 3 + 1
def norm_velc2(r): return 1 - r**2

temp2 = norm_temp2(r2)
velc2 = norm_velc2(r2)

plt.plot(r2, temp2, label="Normalized Temperature")
plt.plot(r2, velc2, label="Normalized Velocity")
plt.legend()
plt.ylabel("Quantity / Quantity$_{max}$")
plt.xlabel("r / R")
plt.savefig("q2.png", dpi=600)
plt.close()
