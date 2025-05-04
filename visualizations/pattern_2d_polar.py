import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 360)
r = np.abs(np.cos(theta))  # Simple cosine pattern

plt.subplot(111, polar=True)
plt.plot(theta, r, label="Cosine Pattern", color='blue')
plt.title("2D Antenna Radiation Pattern")
plt.legend()
plt.savefig("images/polar_pattern.png")
plt.show()
