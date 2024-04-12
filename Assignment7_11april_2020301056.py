#!/usr/bin/env python
# coding: utf-8

# In[4]:


from matplotlib import pyplot as plt


# In[5]:


y=[3,7,5,10]
x=[2,4,6,8]
def bnot(y,x):
    ysum=0
    xsum=0
    for i in range(0,len(y)):
        ysum+=y[i]
        xsum+=x[i]
    ymean=ysum//len(y)
    xmean=xsum//len(x)
    b=slope(y,x)
    a=ymean-(b*xmean)
    return a
def slope(y,x):
    ysum=0
    xsum=0
    for i in range(0,len(y)):
        ysum+=y[i]
        xsum+=x[i]
    ymean=ysum//len(y)
    xmean=xsum//len(x)
    y1=0
    for i in range(0,len(y)):
        y1+=(x[i]*y[i])-(ymean*x[i])
    y2=0
    for i in range(0,len(y)):
        y2+=(x[i]*x[i])-(xmean*x[i])
    return y1//y2
def reg(y,x):
    c=bnot(y,x)
    m=slope(y,x)
    line=[]
    for i in range(0,len(y)):
        line.append(m*x[i]+c)
    return line


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression

x=[2,4,6,8]
y=[3,7,5,10]
x=np.array([2,4,6,8]).reshape(-1,1)
y=np.array([3,7,5,10]).reshape(-1,1)


lr=LinearRegression()
lr.fit(x,y)

x_new=12
x_new = np.array(x_new).reshape(-1, 1)
y_pred=lr.predict(x_new)
print(f"Predicted value of y for x = {x_new}: {y_pred}")

