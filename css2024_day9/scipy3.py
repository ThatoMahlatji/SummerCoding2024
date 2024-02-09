# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:18:39 2024

@author: tjmah
"""

import matplotlib . pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

tlist = np. linspace (0 ,10 ,250)
gmlist = [0.25 , 0.5 , 1.0 , 2.5]
om0 = 2
x0 = 1
v0 = 0

x = lambda gm , Om , t: (x0*np.cos (Om*t) + ((v0 -gm*x0)/Om)*np. sin (Om*t))*np. exp(-gm*t)

fig , ax = plt . subplots ( figsize =(6 ,5) )

for gm in gmlist :
    if om0 >gm:
        Om = np. sqrt ( om0 **2 - gm **2)
    else :
        Om = 1.0j*np. sqrt (gm **2 - om0 **2)

    ax. plot (tlist , x(gm ,Om , tlist ), label =r'$\gamma ={0} $'. format (gm))

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$x(t)$')
ax. legend (loc =0)
plt.show()


# Change initial conditions
x0 = 0
v0 = 1


x = lambda gm , Om , t: (x0*np.cos (Om*t) + ((v0 -gm*x0)/Om)*np. sin (Om*t))*np. exp(-gm*t)

fig , ax = plt . subplots ( figsize =(6 ,5) )

for gm in gmlist :
    if om0 >gm:
        Om = np. sqrt ( om0 **2 - gm **2)
    else :
        Om = 1.0j*np. sqrt (gm **2 - om0 **2)

    ax. plot (tlist , x(gm ,Om , tlist ), label =r'$\gamma ={0} $'. format (gm))

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$x(t)$')
ax. legend (loc =0)
plt.show()

#

x0 = 1
v0 = 0

x = lambda gm , t: (x0 +( v0 + gm*x0)*t)*np. exp (-gm*t)

fig , ax = plt . subplots ( figsize =(6 ,5) )

for gm in gmlist :
    ax. plot (tlist , x(gm , tlist ), label =r'$\ gamma={0} $'. format (gm))

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$x(t)$')
ax. legend (loc =0)
plt.show()

