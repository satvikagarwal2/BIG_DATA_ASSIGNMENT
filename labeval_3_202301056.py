#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('company_sales_data.csv')


# In[3]:


df.head()


# In[4]:


x=df['facecream']
x


# In[5]:


y=df['facewash']
y


# In[16]:


plt.bar(x,y)
plt.show()


# In[17]:


z=df['total_profit']
z


# In[18]:


plt.hist(z)
plt.show


# In[ ]:




