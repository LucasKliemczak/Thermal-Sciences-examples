# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:00:09 2023

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import sin,cos,pi

L = 10 # length of the road
nx = 150 # number of points on the length
Ts = 5  # total time of the simulation
nt = 200  # number of time steps

x = np.linspace(0,L,nx)
k = 0.2  # heat constant
h = L / (nx - 1)
dudt = []

# https://en.wikipedia.org/wiki/Finite_difference_method
def heat_eqn(u,t):
    dudt = np.zeros(x.shape)
    dudt[0] = 0
    dudt[-1] = 0
    for i in range(1, nx-1):
        dudt[i] = k*(u[i-1] - 2*u[i] + u[i+1]) / h**2
    return dudt

max_temp = 150
init_temp = np.ones(x.shape)*max_temp*np.sin(np.pi*x/L)
tspan = np.linspace(0,Ts,nt)
soln = odeint(heat_eqn, init_temp, tspan)

for j in range(len(tspan)):
    plt.clf()
    plt.plot(x,soln[0], label="Initial Temperature")
    plt.plot(x,soln[j], label="Current Temperature")
    heading = 'Time $t$ = ' + str(tspan[j]) + 's,$T_{max}$ = ' + str(np.amax(soln[j]))
    plt.suptitle(heading)
    plt.title("1D Heat Equation")
    plt.xlabel("Length of Rod")
    plt.ylabel('Temperature')
    plt.grid()
    plt.xlim(0,L)
    plt.ylim(0,max_temp+10)
    
    plt.legend()
    plt.pause(0.01)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
