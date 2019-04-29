import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.sqrt(15*x-x*x)
x = np.linspace(0, 15, 1000)
print(x)
y = [f(i) for i in x]
plt.axis([0, 15, 0, 10])
plt.plot(x, y)
plt.show()
