import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
x = 2 * t

plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Week 0 Plot Test")
plt.grid(True)
plt.show()
