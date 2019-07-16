import numpy as np
import matplotlib.pyplot as plt

N = 10
D = 3

X = np.zeros((N,D))
X[:,0] = 1
X[:5,1] = 1
X[5:,2] = 1

print(X)
