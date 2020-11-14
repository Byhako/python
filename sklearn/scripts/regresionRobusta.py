#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding: 0 100px'>
#     <h2 style='padding: 5px; text-align: center'>
#         Regresión Robusta <br />
#         <small>(Lidiar con muchos datos atipicos)</small>
#     </h2>
# </div>

# In[26]:


import pandas as pd
import numpy as np

from sklearn.linear_model import RANSACRegressor, HuberRegressor
from sklearn.svm import SVR # maqina de soporte vectorial

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# In[3]:


data = pd.read_csv('./datasets/felicidad.csv')
data.head()                   


# In[4]:


x = data.drop(['country', 'score'], axis=1)
y = data[['score']]


# In[6]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=37)


# In[7]:


estimadores = {
    'SVR': SVR(gamma='auto', C=0.1, epsilon=0.1),
    'RANSAC': RANSACRegressor(), # Default regresor lineal
    'HUBER': HuberRegressor(epsilon=1.35)
}


# In[35]:


for name, estimador in estimadores.items():
    estimador.fit(x_train, np.array(y_train).ravel())
    prediccion = estimador.predict(x_test)
    
    print(f'Estimador {name}')
    print(f'MSE {mean_squared_error(y_test, prediccion)} \n')


# Vemos que los valorea atipicos afectan mucho el desempeño del modelo SVR

# In[ ]:




