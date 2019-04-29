import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: x**2 + 0.02*np.sin(50*x)
x = np.linspace(-10*np.pi, 10*np.pi,1000)
print(x)
y = [f(i) for i in x]
plt.axis([0, 5, 0, 10])
plt.plot(x, y)
plt.show()
