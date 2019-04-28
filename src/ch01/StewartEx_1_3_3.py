import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: x**2 - 36*x +32
x = np.linspace(-18, 100, 1000)
print(x)
y = [f(i) for i in x]
plt.axis([-20, 50, -300, 500])
plt.plot(x, y)
plt.show()
