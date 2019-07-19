# X is an N*D matrix
# N is num of samples = num of rows
# D is num of features = num of columns
# Y is N-length vector = N*1 column vector

import numpy as np
import matplotlib.pyplot as plt

N = 50

X = np.linspace(0, 10, N)
Y = 0.5*X + np.random.randn(N)

Y[-1] += 30
Y[-2] += 30
print(Y.shape)
print(type(Y))

plt.scatter(X, Y)
plt.show()

# add noise
X = np.vstack([np.ones(N), X]).T

# maxium likelihood
# minimizing error (linear regression) is the same
# as maximizing -1*error

w_ml = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
# To solve w_ml
# w_ml = (((X^T)*X)^(-1))((X^T)*Y)

Yhat_ml = X.dot(w_ml)
# Yhat is the prediction,
# which has the same size as Y

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], Yhat_ml)
plt.show()

# map
l2 = 1000.0
w_map = np.linalg.solve(l2*np.eye(2) + X.T.dot(X), X.T.dot(Y))
# To solve w_map
# w_map = (((lambda*I)+(X^T)*X)^(-1))((X^T)*Y)
# double check L2_regularizationd

Yhat_map = X.dot(w_map)

plt.scatter(X[:,1], Y)
plt.plot(X[:,1], Yhat_ml, label='maxium likelihood')
plt.plot(X[:,1], Yhat_map, label='map')
plt.legend()
plt.show()
