# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 02:23:28 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10)
m=3
c=0
for x in range(10):
 y=m*x+c
 plt.plot(x,y,'r*')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('linear equation')
plt.show()
sin=np.sin(x)
cos=np.cos(y)
plt.subplot(1,2,2)
plt.plot(x,cos,'r+')
plt.subplot(2,2,1)
plt.plot(x,sin,'b*')
plt.show()