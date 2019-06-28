# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,10)
y = np.sin(x)
plt.plot(x,y)
plt.show()
plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Some function of time")
plt.title("My cool chart")
plt.show()
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.show()
plt.plot(x,y)
plt.show()
A = pd.read_csv('D:/jupyterCode/machine_learning_examples/linear_regression_class/data_1d.csv', header = None).as_martrix()
A = pd.read_csv('D:/jupyterCode/machine_learning_examples/linear_regression_class/data_1d.csv', header = None).as_matrix()
x = A[:0]
x = A[:,0]
y = A[:,1]
plt.scatter(x,y)
plt.show()
x_line = np.linspace(0,100,100)
y_line = 2*x_line + 1
plt.scatter(x,y)
plt.plot(x_line, y_line)
plt.show()
plt.hist(x)
plt.show()
R = np.random.random(10000)
plt.hist(R)
plt.show()
plt.his(R, bins=20)
plt.hist(R,bins=20)
plt.show()
y_actual = 2*x + 1
residuals = y - y_actual
plt.hist(residuals)
plt.show()
get_ipython().run_line_magic('save', 'pltPractice 1-42')
