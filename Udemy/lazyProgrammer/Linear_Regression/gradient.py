import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# dj/dw = 2w, initial w = 20, learning rate = 0.1
w = 20
for i in range(30):
    w = w - 0.1*2*w
    print(w)

print("\n")
w = 20
for i in range(100):
    w = w - 0.1*2*w
    print(w)

# J(w1, w2) = w1**2 + w2**4
# dJ/dw1 = 2*w1 + w2**4
# dJ/dw2 = w1**2 + 4*w2**3

print("\n")

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-10,10,0.25)
Y = np.arange(-10,10,0.25)
X, Y = np.meshgrid(X,Y)
Z = X**2 + Y**4
surf = ax.plot_surface(X,Y,Z,cmap='coolwarm', linewidth=0, antialiased=False)
wire = ax.plot_wireframe(X,Y,Z, color='r', linewidth=0.1)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.tight_layout()
plt.show()


w1 = 20
w2 = 20
J = w1**2 + w2**4
djdw1 = 2*w1 + w2**4
djdw2 = w1**2 + 4*w2**3
for i in range(50):
    w1 = w1 - 0.1*(2*w1 + 20**4)
    w2 = w2 - 0.1*(20**2 + 4*w2**3)
    #a = [w1,w2]
    #b = [0.01*djdw1, 0.01*djdw2]
    #np.asarray(a)
    #a = a - [0.01*djdw1, 0.01*djdw2]
    #w1 = np.abs(w1)
    #w2 = w2 - 0.01*djdw2
    #w2 = np.abs(w2)
    print(a)
