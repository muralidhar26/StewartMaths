import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.power(x, 3) - 225*x
x = np.linspace(-20, 20, 10000)
print(x)
y = [f(i) for i in x]
plt.axis([-25, 25, -2000, 2000])
plt.plot(x, y)
plt.show()
