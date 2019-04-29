import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.sin(np.sqrt(x))
x = np.linspace(0, 400*np.pi,1000)
print(x)
y = [f(i) for i in x]
plt.axis([0, 400*np.pi, -1, 1])
plt.plot(x, y)
plt.show()
