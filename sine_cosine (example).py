# Firstly import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np
# This enables us to use (plt) and (np) when we call these two libraries

# Building a set of x values from zero to 4pi in increments of 0.1 radians
x = np.arange(0, 4*np.pi, 0.1) # start, stop, step
y = np.sin(x)
# To create a plot that shows two trig functions, sine and cosine
# We add a third numpy array z which is the cosine of x
z = np.cos(x)
plt.plot(x, y, x, z)

# To add axis labels
plt.xlabel("x values from 0 to 4pi")
plt.ylabel("sin(x) and cos(x)")

# Title
plt.title("Plot of sin and cos from 0 to 4pi")
plt.legend(["sin(x)", "cos(x)"]) # Legend entry
plt.show()

