# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:31:41 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2,100)
fig=plt.figure()
ax=fig.add_axes([.7,.7,.9,.9])
ax.plot(x,x,label='linear')
ax.plot(x,x**2,label='Quadratic')
ax.plot(x,x**3,label='Cubic')
ax.set_xlabel('x label')
ax.set_title('simple plt')
ax.legend()
fig.show()
              
                     