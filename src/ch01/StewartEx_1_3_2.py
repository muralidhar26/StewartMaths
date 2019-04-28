import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.sqrt(x**4 - 16*x*x + 20)
x = np.linspace(-10, 10, 1000)
print(x)
y = [f(i) for i in x]
plt.axis([-10, 10, -10, 10])
plt.plot(x, y)
plt.show()
