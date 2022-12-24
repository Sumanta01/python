# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 23:51:35 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
langs=['c','c++','python','java','css']
students=[33,44,55,38,48]
ax.bar(langs,students)
plt.show()
       