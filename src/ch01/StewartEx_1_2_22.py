import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;


class StewartEx_1_2_22:

    def dataload(self):
        data = [(20, 113), (22, 128), (24, 143), (26, 158), (28, 173), (30, 188), (32, 203), (34, 218), (36, 233)]
        return data


data = StewartEx_1_2_22().dataload()
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
Y_pred_40 = m*40 + c
print ('Y_pred_40-->'+ str(Y_pred_40))

plt.scatter(serX, serY) # actual
plt.plot([min(serX), max(serX)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()