# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 00:16:43 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
data=[[22,33,43,17],[38,23,42,35],[24,55,45,36]]
x=np.arange(4)
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.bar(x+0.00,data[0],color='b',width=0.25)
ax.bar(x+0.25,data[1],color='g',width=0.25)
ax.bar(x+0.25,data[2],color='r',width=0.25)
ax.legend(labels=['cs','It','Et'])
plt.show()