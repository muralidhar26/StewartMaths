import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.divide(x, x*x + 100)
x = np.linspace(0, 100, 10000)
print(x)
y = [f(i) for i in x]
plt.axis([0, 100, 0, 0.1])
plt.plot(x, y)
plt.show()
