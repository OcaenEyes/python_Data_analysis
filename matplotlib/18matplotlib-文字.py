#!/usr/bin/python
#-*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-11,10,1)
y = x*x
plt.plot(x,y)

plt.text(-2,40,'function: y = x*x',
         family = 'serif',size = 20,color='r',style ='italic',weight=0,
         bbox = dict(facecolor = 'b',alpha =0.2)
         )

plt.text(-2,20,'function: y = x*x',
         family ='fantasy',size=20,style = 'oblique',weight=1000
         )

plt.show()