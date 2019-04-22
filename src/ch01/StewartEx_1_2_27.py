import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;
import math as math


class StewartEx_1_2_27:

    def dataload(self):
        data = [(10, 5), (104, 9), (8958, 40), (11423, 39), (76184, 84), (114511, 76)]
        return data


data = StewartEx_1_2_27().dataload()
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

Y_pred_754 = m*np.log10(754) + c

print("Y_pred_754-->"+str(np.power(10, Y_pred_754)))