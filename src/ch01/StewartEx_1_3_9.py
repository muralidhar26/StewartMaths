import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.sin(1000*x)**2
x = np.linspace(-np.pi/500, np.pi/500, 10000)
print(x)
y = [f(i) for i in x]
plt.axis([-np.pi/500, np.pi/500, 0, 1])
plt.plot(x, y)
plt.show()
