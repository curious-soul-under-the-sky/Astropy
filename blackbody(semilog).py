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


w_micro = np.linspace(0.03, 30, 3000)
w = w_micro * 10 ** (-6)

temps = [100, 200, 2000, 4000, 8000, 10000, 30000]


for temp in temps:
    plt.semilogy(w_micro, plancklaw(w, temp))

plt.ylim(10 ** (3), 10 ** (19))
plt.xlabel("Wavelength (micrometers)")
plt.ylabel("Spectral Radiance (log scale)")

plt.grid('..')

plt.title("Planck Black Body Radiation")

plt.savefig('plank_law_01.png', dpi=100, facecolor='white')

plt.show()
