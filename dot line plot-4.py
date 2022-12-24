# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:00:07 2022

@author: KIIT
"""

from matplotlib import pyplot as plt
from numpy import*
x=linspace(-3,3,30)
y=x**2
plt.plot(x,y,'r.')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('x-y plot using linespace !')
plt.show()