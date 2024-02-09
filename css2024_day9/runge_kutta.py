# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:47:21 2024

@author: tjmah
"""
import matplotlib.pyplot as plt

h = 0.1 # step size
x0 = 0 # initial x- value
xmax = 0.5 # final x- value
y0 = 1 # initial y- value

y_rk2 = [y0]
x_list = [x0]
f = lambda x,y: 2*y **(3/2)

while x0 <= xmax :
    print("x0 = ", x0)
    a1 = f(x0 ,y0)*h
    a2 = f(x0 + h, y0 + a1)*h
    y1 = y0 + 0.5 * (a1 + a2)
    
    y_rk2 . append (y1)
    print("y = ", y1)
    y0=y1
    x0 = round (x0+h ,10)
    x_list.append(x0)


plt.plot(x_list,y_rk2)
plt.show()
