# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:45:08 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
from numpy import*
x=linspace(-3,3,30)
y=x**2
plt.plot(x,y,'r.')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('x-y plot using linespace!')
plt.show()
