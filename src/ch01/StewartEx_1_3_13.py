import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: 10*np.sin(x) + np.sin(100*x)
x = np.linspace(-np.pi/25, np.pi/25,100)
print(x)
y = [f(i) for i in x]
plt.axis([-np.pi/25, np.pi/25, -1, 1])
plt.plot(x, y)
plt.show()
