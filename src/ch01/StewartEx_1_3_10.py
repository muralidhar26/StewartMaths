import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.cos(0.001*x)
x = np.linspace(-np.pi*2000, np.pi*2000, 10000)
print(x)
y = [f(i) for i in x]
plt.axis([-np.pi*2000, np.pi*2000, -1, 1])
plt.plot(x, y)
plt.show()
