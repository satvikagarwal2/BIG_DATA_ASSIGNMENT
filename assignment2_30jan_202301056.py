# -*- coding: utf-8 -*-
"""assignment2_30jan_202301045.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-msE-1LOqQwuMTmgy8X6yl4RiunRDnXz
"""

import numpy as np
import math as mt

import numpy as np
arr=np.array([1,2,3,6,4,5])
arr[::-1]

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])
arr1==arr2

x=np.array ([1,2,3,4,5,1,2,1,1,1])
y=np.array ([1,1,1,2,3,4,2,4,3,3])
def mostFrequent(x,n):
  Hash = dict()
  for i in range(n):
    if arr[i] in Hash.keys():
      Hash[arr [i]] += 1
    else:
      Hash[arr[i]]=1
      max_count = 0
      res=-1
      for i in Hash:
        if (max_count < Hash[i]):
          res = i
          max_count - Hash[i]
          return res

gfg=np.matrix([4,1,9,12,3,1,4,5,6])
print(np.sum(gfg))
print(np.sum(gfg,axis=1))
print(np.sum(gfg,axis=0))