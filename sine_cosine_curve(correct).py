import matplotlib.pyplot as plt
import numpy as np


t = np.arange(-2*np.pi, 2*np.pi, 0.2)

plt.plot(t, np.sin(t), label = "sin", linestyle = "-.")
plt.plot(t, np.cos(t), label = "cos", linestyle = ":")

plt.title("sin and cos graph")
plt.xlabel("angle")
plt.ylabel("sin and cos value")
plt.legend()
plt.show()