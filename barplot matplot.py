# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:12:41 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([2,4,6,8])
langs=['c','c++','java','python','php']
students=[10,15,20,25,30]
ax.bar(langs,students)
plt.show()