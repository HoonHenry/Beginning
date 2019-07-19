import numpy as np
import matplotlib.pyplot as plt

address = "D:\HoonsCode\machine_learning_examples\linear_regression_class\data_poly.csv"

X = []
Y = []
for line in open(address):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x*x])
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X[:,1], Y)
plt.show()

w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, w)

plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.show()

d1 = Y -Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d2) / d2.dot(d2)
print("r-squared: ", r2)
