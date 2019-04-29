import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: np.sqrt(50-0.2*x)
x = np.linspace(-250, 250, 1000)
print(x)
y = [f(i) for i in x]
plt.axis([-250, 250, 0, 12])
plt.plot(x, y)
plt.show()
