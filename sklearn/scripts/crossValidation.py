#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding:0'>
# <h2 style='margin:20px; text-align:center'>Validación Cruzada</h2>
# </div>

# In[1]:


import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold


# In[2]:


data = pd.read_csv('./datasets/felicidad.csv')
data.head()


# In[3]:


x = data.drop(['country', 'score'], axis=1)
y = data['score']


# In[4]:


model = DecisionTreeRegressor()
score = cross_val_score(model, x, y, scoring='neg_mean_squared_error', cv=5)
score


# Entre mas cercano a cero mejor es el modelo

# In[5]:


np.abs(np.mean(score)) # score promedio


# In[6]:


kf = KFold(n_splits=3, shuffle=True, random_state=42)
for train, test in kf.split(data):
    print(f'\nTrain: {train}\n\n Test: {test}\n')
    print('='*32)


# Cada array tiene los inices de los datos en el dataset segun cada partición

# # Optimizacion Paramétrica

# <ul>
# <li>Optimizacion manual</li>
#     <ol>
#         <li>Escojer el modelo para ajustar.</li>
#         <li>Buscar en la documentación de sklearn</li>
#         <li>Identificar los posibles ajustes.</li>
#         <li>Probar combinaciones una por un aiterando a través de listas</li>
#     </ol><br />
# <li>Grilla de parametros (GridSeachCV)</li>
#     <ol>
#         <li>Definir una o varias variables que queremos optimizar</li>
#         <li>Identificar los posibles valores que pueden tener los parametros</li>
#         <li>Crear un diccionario de parametros</li>
#         <li>Usar cross validation</li>
#         <li>Entrenar el modelo.</li>
#     </ol><br />
# <li>Búsqueda aleatoria (RandomizedSeacrhCV)</li>
#     <ol>
#         <li>Definir una o varias variables que queremos optimizar</li>
#         <li>Identificar los rangos de valores que pueden tomar ciertos parametros</li>
#         <li>Crear un diccionario de rangos de valores</li>
#         <li>Usar cross validation</li>
#         <li>Entrenar el modelo.</li>
#     </ol><br />
# </ul>

# In[11]:


from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor


# ### RandomizedSeacrhCV

# In[15]:


x = data.drop(['country', 'score', 'rank'], axis=1)
y = data['score']

reg = RandomForestRegressor()
params = {
    'n_estimators': range(4, 16), # Escoge el mejor numero de estimadores
    'criterion': ['mse', 'mae'],  # Medida de calidad de los splits
    'max_depth': range(2, 11)     # Profundidad del arbol
}

rand_est = RandomizedSearchCV(
        reg,
        params,
        n_iter=10,
        cv=3,
        scoring='neg_mean_absolute_error',
        iid=True
)

rand_est.fit(x, y)


# In[18]:


print(f'Best Estimator:\n {rand_est.best_estimator_}')


# In[17]:


print(f'Best Params:\n {rand_est.best_params_}')


# In[20]:


print(f'Prediction:\n {rand_est.predict(x.loc[[0]])}')


# In[ ]:




