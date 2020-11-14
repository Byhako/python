#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding:0 100px;'>
#     <h1 style='text-align:center; padding: 5px'>
#         Analisis de componentes principales
#     </h1>
# </div>

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.despine()

import pandas as pd
import sklearn

# Analisis de componentes principales
from sklearn.decomposition import PCA, IncrementalPCA

# Clasificador lineal
from sklearn.linear_model import LogisticRegression

# Escalador para normalizar datos
from sklearn.preprocessing import StandardScaler

# Division de datos
from sklearn.model_selection import train_test_split


# In[3]:


dt_heart = pd.read_csv('./datasets/heart.csv')
dt_heart.head()


# In[4]:


dt_features = dt_heart.drop(['target'], axis=1)
dt_target = dt_heart['target']

# Normalizamos datos
dt_features = StandardScaler().fit_transform(dt_features)

# Partimos conjunto de entrenamiento
x_train, x_test, y_train, y_test = train_test_split(
    dt_features,
    dt_target,
    test_size=0.3,
    random_state=41
)
print('Datos X: ', x_train.shape)
print('Datos y: ', y_train.shape)


# In[5]:


# n_components = min(n_muestras, n_features) // default
pca = PCA(n_components=3)
pca.fit(x_train, y_train)

# Entrena por bloques no con todos los datos a la vez
ipca = IncrementalPCA(n_components=3, batch_size=10)
ipca.fit(x_train, y_train)


# In[9]:


plt.scatter(range(len(pca.explained_variance_)), pca.explained_variance_ratio_)
plt.show()


# ### Vemos que las dos primeras componentes son las que mas información aportan.  Ahora configuraremos la regresión logística para comparar.

# In[19]:


logistic = LogisticRegression(solver='lbfgs')

## Debemos aplicar pca en el conjunto de entrenamiento y en el de pruebas
dt_train = pca.transform(x_train)
dt_test = pca.transform(x_test)

logistic.fit(dt_train, y_train)

## Calculemos metricas para comparar
print(f'Score PCA: {logistic.score(dt_test, y_test)}')

## Ahora lo mismo pero con ipca
dt_train = ipca.transform(x_train)
dt_test = ipca.transform(x_test)

logistic.fit(dt_train, y_train)

## Calculemos metricas para comparar
print(f'Score IPCA: {logistic.score(dt_test, y_test)}')


# In[ ]:




