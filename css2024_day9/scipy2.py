# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:57:29 2024

@author: tjmah
"""

import numpy as np
from scipy . integrate import solve_ivp
import matplotlib.pyplot as plt

k1 = 0.1
k2 = 0.4

# Right - hand side of ODE
def f(t,y):
    # y is 2d- array
    dydt = [y[1] , -k1*y [1] - k2*np. sin (y [0]) ]
    return dydt

# t- values for which ODE is solved
t_eval = np. linspace (0, 100 , 300)

sol = solve_ivp (f, [ t_eval [0] , t_eval [ -1]] ,
                 y0 =[1 ,0] , method ='RK45', t_eval = t_eval )

y1 = sol.y[0 ,:]
y2 = sol.y[1 ,:]

plt.figure()
plt.plot(t_eval,y1)
plt.plot(t_eval,y2)
plt.legend(["y1","y2"])
plt.show()


plt.figure()
plt.plot(y1,y2)
plt.title("Phase plot")
plt.show()
