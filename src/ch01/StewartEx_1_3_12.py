import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: 1/(np.cos(20*np.pi*x))
x = np.linspace(-0.25, 0.25,1000)
print(x)
y = [f(i) for i in x]
plt.axis([-0.25, 0.25, -250, 750])
plt.plot(x, y)
plt.show()
