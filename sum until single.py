# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:14:03 2022

#@author: KIIT
import math
class Solution:
   def solve(self, n):
      if n < 10:
         return n
      s = 0
      l = math.floor(math.log(n, 10) + 1)
      while l > 0:
         s += n % 10
         n //= 10
         l -= 1
      return self.solve(s)
ob = Solution()
print(ob.solve(9625))
    
    
    
      