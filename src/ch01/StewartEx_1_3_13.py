import numpy as np
import matplotlib.pyplot as plt

# plt.plot([-2, 2], [-2, 2], 'ro')
f = lambda x: 10*np.sin(x) + np.sin(100*x)
x = np.linspace(-2*np.pi, 2*np.pi,100)
print(x)
y = [f(i) for i in x]
plt.axis([-2*np.pi, 2*np.pi, -14, 14])
plt.plot(x, y)
plt.show()
