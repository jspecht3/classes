import numpy as np

# question 3b
mu = 5e-16 # A*m^2
b = 50e-6 # T
t = 300 # K
k = 1.380649e-23 # J/K

avg_cos = 1 / np.tanh(mu * b / k / t) - k * t / mu / b
avg_rad = np.arccos(avg_cos)
avg_deg = np.degrees(avg_rad)

print(f"Average Cos:   {round(avg_cos, 5)}")
print(f"Average Theta: {round(avg_rad, 5)} rad")
print(f"Average Theta: {round(avg_deg, 5)} deg")
