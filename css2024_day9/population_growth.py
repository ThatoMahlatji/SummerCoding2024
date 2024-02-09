# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:16:45 2024

@author: tjmah
"""

import matplotlib . pyplot as plt
import numpy as np

tlist = np. linspace (0 ,50 ,150)
rlist = [0.1 , 0.25 , 0.5 , 1.0]

p0 = 1 # initial popluation
k = 5 # equilibrium population

fig , ax = plt . subplots ( figsize =(4 ,5) )

for r in rlist :
    ax. plot (tlist , k + (p0 -k)*np. exp (-r* tlist ), 
              label =r'$r ={0} $'. format (r))
    ax. axhline (k, tlist [0] , tlist [ -1] ,
                 linestyle='--', c='k')

ax. set_xlabel (r'$t$ ')
ax. set_ylabel (r'$p(t)$')
ax. legend (loc =0)

print("\n------------\n")

tlist = np. linspace (0 ,10)
klist = [1.5 , 1.7 , 1.8 , 1.85]

p0 = 1 # initial popluation
r = 1 # growth rate

fig , ax = plt . subplots ( figsize =(4 ,5) )

for k in klist :
    ax. plot (tlist , k + (p0 -k)*np. exp (-r* tlist ),
              label =r'$k ={0} $'. format (k))
    ax. axhline (k, tlist [0] , tlist [ -1] , 
                 linestyle='--', c='k')

ax. set_xlabel (r'$t$')
ax. set_ylabel (r'$p(t)$')
ax. legend (loc =0)
plt.show()