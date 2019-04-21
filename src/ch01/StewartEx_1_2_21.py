import matplotlib.pyplot as plt
import pandas as pd
import numpy as np;


class StewartEx_1_2_21:

    def dataload(self):
        data = [(4000, 14,1), (6000, 13.0), (8000, 13.4), (12000, 12.5), (16000, 12.0), (20000, 12.4), (30000, 10.5), (45000, 9.4), (60000, 8.2)]
        return data


data = StewartEx_1_2_21().dataload()
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
Y_pred_25000 = m*25000 + c
print ('Y_pred_25000-->'+ str(Y_pred_25000))
Y_pred_80000 = m*80000 + c
print ('Y_pred_80000-->'+ str(Y_pred_80000))
Y_pred_200000 = m*200000 + c
print ('Y_pred_200000-->'+ str(Y_pred_200000))

plt.scatter(serX, serY) # actual
# plt.scatter(X, Y_pred, color='red')
plt.plot([max(serX), min(serX)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()


