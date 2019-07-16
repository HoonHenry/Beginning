import numpy as np
import matplotlib.pyplot as plt

N = 50
D = 50

X = (np.random.random((N, D)) - 0.5)*10

true_W = np.array([1, 0.5, -0.5] + [0]*(D-3))

Y = X.dot(true_W) + np.random.randn(N)*0.5

costs = []
W = np.random.randn(D) / np.sqrt(D)
learning_rate = 0.001
l1 = 10.0
for t in range(500):
    Yhat = X.dot(W)
    delta = Yhat - Y
    W = W - learning_rate*(X.T.dot(delta) + l1*np.sign(W))

    mse = delta.dot(delta) / N
    costs.append(mse)

plt.plot(costs)
plt.show()

print("final W: ", W)

plt.plot(true_W, label='true W')
plt.plot(W, label='W_map')
plt.legend()
plt.show()
