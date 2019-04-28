import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: x**3+15*x*x+65*x
x = np.linspace(-10, 5, 1000)
print(x)
y = [f(i) for i in x]
plt.axis([-10, 5, -100, 500])
plt.plot(x, y)
plt.show()
