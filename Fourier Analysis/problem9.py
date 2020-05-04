"""
Code segment for problem 9

The scritp was in 2017 translated by Sebastian G. Winther-Larsen from a matlab script originally written by Arnt Inge Vistnes
"""

import numpy as np

freq = 100  # Frequency in hertz
t = 4
x = 0.8 * np.cos(2*np.pi*freq*t)  # Simple cosine signal
print(x)
