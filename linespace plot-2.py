# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 00:38:17 2022

@author: KIIT
"""

from matplotlib import pyplot as plt
import numpy as np
import math
x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("Angle")
plt.ylabel("Sine")
plt.title("Sine wave")
plt.show()
