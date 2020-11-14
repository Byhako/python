#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding: 0'>
#     <h2 style='margin: 20px; text-align: center'>
#         Métodos de ensamble
#     </h2>
# </div>

# * Bagging: Bootstrab AGGgragation  (expertos en paralelo)
#     * Random forest
#     * voting classifiers / regressors
#     
# * Boosting (expertos en serie)
#     * adaBoost
#     * gradient tree boosting
#     * XGBoost

# In[12]:


import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


data = pd.read_csv('./datasets//heart.csv')
data.head()


# In[5]:


x = data.drop(['target'], axis=1)
y = data[['target']]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.35)


# <div class='alert alert-success' style='padding:0px'>
#     <h3 style='margin: 5px 20px'>Bagging</h3>
# </div>

# In[9]:


knn = KNeighborsClassifier().fit(x_train, np.array(y_train).ravel())
knn_predict = knn.predict(x_test)
print(f'Score: {accuracy_score(knn_predict, y_test)}')


# In[11]:


bag = BaggingClassifier(base_estimator=KNeighborsClassifier(), n_estimators=50).fit(x_train, np.array(y_train).ravel())
bag_predict = bag.predict(x_test)
print(f'Bagging {accuracy_score(bag_predict, y_test)}')


# Vemos que con el metodo de ensamble mejoro la exactitud

# <div class='alert alert-success' style='padding: 0'>
#     <h3 style='margin: 5px 20px'>Boosting</h3>
#     </div>

# In[13]:


boost = GradientBoostingClassifier(n_estimators=50) # Usa arboles de decision pequeños
boost.fit(x_train, np.array(y_train).ravel())
boost_predict = boost.predict(x_test)
print(f'Boosting {accuracy_score(boost_predict, y_test)}')


# In[ ]:




