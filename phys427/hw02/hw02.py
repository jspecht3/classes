import numpy as np
import matplotlib.pyplot as plt

# question 1
gamma = np.linspace(0.0, 1, 100)
sigma = gamma * np.log(1 - gamma) - np.log(1 - gamma) - gamma * np.log(gamma)
sigma[0], sigma[-1] = 0, 0


plt.plot(gamma, sigma)
plt.show()
