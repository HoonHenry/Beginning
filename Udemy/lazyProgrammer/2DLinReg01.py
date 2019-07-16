import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
address = "D:\HoonsCode\machine_learning_examples\linear_regression_class\data_2d.csv"
for line in open(address):
    x1, x2, y = line.split(',')
    X.append([1, float(x1), float(x2)])
    Y.append(float(y))

# turn X and Y into numpy array
X = np.array(X)
Y = np.array(Y)

# let's plot the data to see what time data looks like
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X[:,0], X[:,1], Y)
# plt.show()

# calculate weight
W = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, W)

# compute r-squared
d1 = Y -Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d2) / d2.dot(d2)
print("r-squared: ", r2)
