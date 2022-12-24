# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:56:52 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(1,1)
a=np.aray,bins=([8,33,44,55,66,6,32,65,76,87,99,23,43,41,76,98,43,65,54])
ax.hist(a,bins=[0,65,76,34,55])
ax.set_title("histogram of result:")
#ax.set_xticks([0,23,45,54,76])
ax.set_xlabel('marks')
ax.set_ylabel('no.of students')
plt.show()