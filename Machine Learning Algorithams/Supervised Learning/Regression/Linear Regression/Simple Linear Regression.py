#!/usr/bin/env python
# coding: utf-8

# Simple linear regression is a regression model that estimates the relationship between one independent variable and one dependent variable using a straight line. Both variables should be quantitative.

# # Step 1: Data Preprocessing

# In[24]:


#import libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('student_scores.csv')

#Initialising the X axis and Y axis 
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values


# In[25]:


from sklearn.model_selection import train_test_split
#Use train_test_split() to get training and test sets
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) #


# # Step 2: Fitting Simple Linear Regression Model to the training set

# In[26]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)


# # Step 3: Predecting the Result

# In[14]:


Y_pred = regressor.predict(X_test)


# # Step 4: Visualization

# ### Visualising the Training results

# In[30]:


#visulization train results using the matplotlib 
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='black')


# In[31]:


#Visualizing the test results
plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='black')


# In[ ]:




