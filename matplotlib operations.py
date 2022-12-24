# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:54:43 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10)
y=np.arange(11,21)

a=np.arange(40,50)
b=np.arange(50,60)


plt.scatter(x,y,c='r')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('2D Graph')
plt.show()
y=x*x
plt.plot(x,y,'g*',linestyle='dashed',linewidth=2,markersize=12)
# SUBPLOT
plt.subplot(2,2,1)
plt.plot(x,y,'r+')
plt.subplot(2,2,2)
plt.plot(x,y,'g--')
plt.subplot(2,2,3)
plt.plot(x,y,'b*-')
# equation


