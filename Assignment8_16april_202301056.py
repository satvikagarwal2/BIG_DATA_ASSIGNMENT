#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
df = pd.read_csv("data.csv")


# In[2]:


df


# In[3]:


X = df[['Weight', 'Volume']]
y = df['CO2']


# In[4]:


X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)


# In[7]:


reg_model = linear_model.LinearRegression()
reg_model = LinearRegression().fit(X_train, y_train)


# In[8]:


y_pred= reg_model.predict(X_test)  
x_pred= reg_model.predict(X_train) 


# In[9]:


reg_model_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred})
reg_model_diff


# In[ ]:




