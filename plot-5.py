# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:07:15 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
from numpy import *
x=linspace(-3, 3 ,30)
y= x**2
plt.plot(x, sin(x))
plt.plot(x,cos(x),'r-')
plt.plot(x,-sin(x),'g--')
plt.plot(x,-cos(x),'h')
plt.xlabel("x-axis")
plt.ylabel("y- axis")
plt.title("x-y plot using linspace")
plt.show()



