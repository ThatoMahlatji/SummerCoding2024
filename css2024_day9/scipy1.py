# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:34:38 2024

@author: tjmah
"""
"""-----Scipy------"""
# Link: https://docs.scipy.org/doc/scipy/index.html


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Right - hand side of ODE
f = lambda t,y: np. sin (t) **2 * y

# t- values for which ODE is solved
t_eval = np. linspace (0, 10)

sol = solve_ivp(f, [ t_eval [0] , t_eval [ -1]] ,
                 y0 =[1] , method ='RK45', t_eval = t_eval )

sol .t # Returns t- values shape =( len ( t_eval ) ,)
sol .y # Returns y- values shape =( len (y0),len (t_eval ))

sol .y. reshape ( sol .t. shape ) # shape =( len ( t_eval ) ,)


plt.plot(sol.t,sol .y. reshape ( sol .t. shape ))

actual = lambda t:np.exp(0.5*(t - 0.5*np.sin(2*t)))

plt.plot(t_eval,actual(t_eval))
plt.legend(["RK45","Exact"])

plt.show()

