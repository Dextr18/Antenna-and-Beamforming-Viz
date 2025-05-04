import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi, np.pi, 1000)
N = 8
d = 0.5
beta = np.pi / 4  # Steering angle

AF = np.abs(np.sum([
    np.exp(1j * 2 * np.pi * d * n * np.sin(theta - beta)) for n in range(N)
], axis=0))

AF /= np.max(AF)

plt.polar(theta, AF, color='green')
plt.title("Beamforming Array Pattern (Steered π/4)")
plt.savefig("images/beamforming_array.png")
plt.show()
