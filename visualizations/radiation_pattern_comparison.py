import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 360)
dipole = np.abs(np.sin(theta))
isotropic = np.ones_like(theta)

plt.polar(theta, isotropic, '--', label='Isotropic', color='gray')
plt.polar(theta, dipole, label='Dipole', color='purple')
plt.title("Isotropic vs Dipole Radiation")
plt.legend(loc='upper right')
plt.savefig("images/pattern_comparison.png")
plt.show()
