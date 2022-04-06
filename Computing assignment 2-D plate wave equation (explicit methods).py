# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:50:02 2022

@author: adity
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

size = 10  #size of the square plate
dx = 0.1
x = np.arange(0,size+dx,dx)
y = np.arange(0,size+dx,dx)
X,Y = np.meshgrid(x,y)
T = 10


r = 0.7 #r = cdt/dx
s = 1
dt = (r*dx)/s
image = np.zeros((len(x),len(y),int(T/dt)+1))

u = np.zeros((len(y),len(x)))
m, n = len(u) - 1, len(u[0]) - 1  # m is length of rows, n is length of columns
next_u = u.copy()
prev_u = u.copy()
image[:,:,0] = u

t = 0
c = -1

while t < T:
    u[0,:] = 0
    u[:,0] = 0
    u[m,:] = 0
    u[:,n] = 0

    t = t+dt
    c += 1
    prev_u = u.copy() # When updating lists use .copy() instead of just saying prev_u = u, this is because python suffers from a problem in parallel computing
    u = next_u.copy() # Same as stated above
    image[:,:,c] = u
    
    u[int(m/2)][int(n/2)] = (dt**2)*20*np.sin(30*np.pi*t/20)
    
    for i in range(1,m):
        for j in range(1,n):
            next_u[i][j] = 2*u[i][j] - prev_u[i][j] + (r**2)*(u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - 4*u[i][j])


for l in range(0,c,3):
    fig = plt.figure(figsize = [12,8])
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(X,Y,image[:,:,l], cmap = cm.coolwarm, vmin = -0.01, vmax = 0.01)
    ax.set_zlim([-0.05,0.05])
    fig.colorbar(surf)                         #Add a colorbar to the plot
    ax.view_init(elev=30,azim=45)              #Elevation & angle initial vi
    #Axis limits and labels.
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

for x in range(0,c,3):
   fig, ax = plt.subplots(figsize=(12,8))
   ax.set_aspect('equal')
   cf = ax.contourf(X,Y,image[:,:,x])
   fig.colorbar(cf, ax=ax)
   plt.show()


   










