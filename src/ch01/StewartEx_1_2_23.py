import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;


class StewartEx_1_2_23:

    def dataload(self):
        data = [(1896, 3.3), (1900, 3.3), (1904, 3.5), (1908, 3.71), (1912, 3.95), (1920, 4.09), (1924, 3.95),
                (1928, 4.2), (1932, 4.31), (1936, 4.35), (1948, 4.3), (1952, 4.55), (1956, 4.56), (1960, 4.7),
                (1964, 5.1), (1968, 5.4), (1972, 5.64), (1976, 5.64), (1980, 5.78), (1984, 5.75), (1988, 5.9),
                (1992, 5.87), (1996, 5.92), (2000, 5.9), (2004, 5.95)]
        return data


data = StewartEx_1_2_23().dataload()
x_val = [x[0] for x in data]
y_val = [x[1] for x in data]

dataX = np.array(x_val)
dataY = np.array(y_val)
serX = pd.Series(dataX)
serY = pd.Series(dataY)
X_mean = np.mean(dataX)
Y_mean = np.mean(dataY)

# Method of lease squares

numerator = 0;
denominator = 0;
for i in range(len(dataX)):
    numerator += (dataX[i] - X_mean) * (dataY[i] - Y_mean)
    denominator += (dataX[i] - X_mean)**2

m = numerator / denominator
c = Y_mean - m*X_mean

print (m, c)

Y_pred = m*dataX + c
Y_pred_2008 = m*2008 + c
print ('Y_pred_2008-->'+ str(Y_pred_2008))

plt.scatter(serX, serY) # actual
plt.plot([min(serX), max(serX)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()