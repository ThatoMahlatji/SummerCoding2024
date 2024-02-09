# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:19:17 2024

@author: tjmah

"""

# Link (Quad): https://docs.scipy.org/doc/scipy/reference/integrate.html

import matplotlib . pyplot as plt
import numpy as np

print("---------Homogenous---------")

td_list = [0.5 , 1.0 , 2.0 , 4.0]
tlist = np. linspace (0 ,10)

# Parameters
q0 = 5

fig , ax = plt . subplots ()
for td in td_list :
    ax. plot (tlist , q0*np. exp(- tlist /td), 
              label =r'$t_d={0} $'. format (td))

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$q(t)$')
ax. legend (loc =0)
plt.show()

print("---------Inhomogenous---------")
'''
import matplotlib . pyplot as plt
import numpy as np
from scipy . integrate import quad

td_list = [0.5 , 1.0 , 2.0 , 4.0]
tlist = np. linspace (0 ,10)

# Parameters
q0 = 5
V0 = 4
om = 2

fig , ax = plt . subplots ()
for td in td_list :
    qlist = []
    err_list = []
    integrand = lambda x, t: V0*np.sin (om*x)*np. exp ((-t-x)/td)
    for t in tlist :
        q, _ = q0*np. exp (-t/( td)) + quad ( integrand , t,0, args =(t ,))
        qlist . append (q)
        ax. plot (tlist , qlist , label =r'$t_d ={0} $'. format (td))

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$q(t)$')
ax. legend (loc =0)
'''
print("Needs fixing")