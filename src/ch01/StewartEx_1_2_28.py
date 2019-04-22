import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;
import math as math


class StewartEx_1_2_28:

    def dataload(self):
        data = [(0.387, 0.241), (0.723, 0.615), (1.000, 1.000), (1.523, 1.881), (5.203, 11.861),
                (9.541, 29.457), (19.190, 84.008), (30.086, 164.784)]
        return data


data = StewartEx_1_2_28().dataload()
x_val = np.log10([x[0] for x in data])
y_val = np.log10([x[1] for x in data])

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

print ("The coefficients are--> "+str(m) + ", "+ str(np.power(10, c)))

Y_pred = m*dataX + c
print(np.power(10, y_val))
print (np.power(10, Y_pred))