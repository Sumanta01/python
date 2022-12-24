# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:11:59 2022

@author: KIIT
"""

import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.axis('equal')
years=['2001','2002','2004','2004','2005']
students=[23945,12356,43467,27244,32744]
ax.pie(students,labels=years,autopct='%6.2f%%')
plt.show()