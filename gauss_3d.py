#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 30

x1 = 0.1*np.random.randn(N,4) + np.array([1,2,-1,0])
x2 = 0.1*np.random.randn(N,4) + np.array([-1,2,1,0])
x3 = 0.1*np.random.randn(N,4) + np.array([1,-2,-1,0])
x4 = 0.1*np.random.randn(N,4) + np.array([-1,-2,1,0])

data = np.empty((0, 2))
data = np.vstack((x1, x2, x3, x4))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0], data[:,1], data[:,2], c='b', marker='o')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.set_title('Original Clustering')
plt.show()



np.savetxt('./gauss_4_3d.csv', data, delimiter=',')
