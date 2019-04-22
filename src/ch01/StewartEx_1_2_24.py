import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;


class StewartEx_1_2_24:

    def dataload(self):
        data = [(1955, 30.4), (1960, 26.4), (1965, 23.6), (1970, 21.1), (1975, 19.0), (1980, 17.1), (1985, 15.0), (1990, 13.0), (1995, 11.7), (2000, 10.5)]
        return data


data = StewartEx_1_2_24().dataload()
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
Y_pred_1988 = m*1988 + c
print ('Y_pred_1988-->'+ str(Y_pred_1988))
Y_pred_2002 = m*2002 + c
print ('Y_pred_2002-->'+ str(Y_pred_2002))

plt.scatter(serX, serY) # actual
plt.plot([max(serX), min(serX)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()