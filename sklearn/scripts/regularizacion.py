#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding: 0 100px'>
#     <h2 style='padding: 5px; text-align: center'>
#         Regularización
#     </h2>
# </div>

# In[2]:


import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# In[3]:


data = pd.read_csv('./datasets/felicidad.csv')
data.head()


# In[4]:


x = data[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
y = data[['score']]

print(f'shape x: {x.shape}')
print(f'shape y: {y.shape}')


# In[5]:


xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=30)


# ## Definiendo los regresores

# In[7]:


modelLinear = LinearRegression().fit(xTrain, yTrain)
y_linear = modelLinear.predict(xTest)

# a mayor alpha mayor penalizacion

# Regularización L1, Lasso, Least Absolute Shrinkage and Selection Operator
modelLasso = Lasso(alpha=0.02).fit(xTrain, yTrain)
y_lasso = modelLasso.predict(xTest)

# Regularización L2,  No lleva ningun parametro a cero
modelRidge = Ridge(alpha=1).fit(xTrain, yTrain)
y_ridge = modelRidge.predict(xTest)


# ## Medimos la eficiencia de cada modelo

# In[8]:


linear_lost = mean_squared_error(yTest, y_linear)
lasso_lost = mean_squared_error(yTest, y_lasso)
ridge_lost = mean_squared_error(yTest, y_ridge)

print(f'Linear lost {linear_lost}')
print(f'Lasso lost {lasso_lost}')
print(f'Ridge lost {ridge_lost}')


# In[10]:


print(f'Coeficientes modelo linear\n {modelLinear.coef_}\n')
print(f'Coeficientes modelo lasso\n {modelLasso.coef_}\n')
print(f'Coeficientes modelo ridge\n {modelRidge.coef_}\n')


# Como vemos el modelo lineal (sin regularización) fue el mejor ya que tiene la menor perdida. Con respecto a los coeficientes, cada uno coresponde a cada columna del modelo, y entre mas pequeño el número, menor peso tiene dentro del modelo.  Lasso funciona mejor cuando tenemos pocos features, y ridge cuendo tenemos muchos. Un modelo intermedio entre los dos es elasticNet

# In[ ]:




