import matplotlib.pyplot as plt
import numpy as np
from scipy import constants

h = constants.h
k = constants.k
c = constants.speed_of_light


def plancklaw(w, T):
    num = 2 * h * c ** 2
    den = w ** 5 * (np.exp((h * c) / (k * w * T)) - 1)
    radiance = num / den
    return radiance


w_micro = np.linspace(0.03, 0.6, 3000)
w = w_micro * 10 ** (-6)

temps = [10000, 30000]

for temp in temps:
    plt.plot(w_micro, plancklaw(w, temp))

plt.xlabel("Wavelength (micrometers)")
plt.ylabel("Spectral Radiance (W/ m2 sr Hz)")

plt.grid('..')

plt.title("Planck Black Body Radiation")

plt.savefig('plank_law_01.png', dpi=1000, facecolor='white')

plt.show()
