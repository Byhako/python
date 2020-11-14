#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding:0 100px;'>
#     <h1 style='text-align:center; padding: 5px'>
#         Clasificador con Kernel
#     </h1>
# </div>

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import seaborn as sns
sns.set_style('darkgrid')
sns.despine()

# Analisis de componentes principales
from sklearn.decomposition import KernelPCA

# Clasificador lineal
from sklearn.linear_model import LogisticRegression

# Escalador para normalizar datos
from sklearn.preprocessing import StandardScaler

# Division de datos
from sklearn.model_selection import train_test_split


# In[2]:


dt_heart = pd.read_csv('./datasets/heart.csv')
dt_heart.head()


# In[3]:


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


# In[6]:


# kernel =  linear, poly, rbf 
kpca = KernelPCA(n_components=4, kernel='poly')
kpca.fit(x_train)

dt_train = kpca.transform(x_train)
dt_test = kpca.transform(x_test)

logistic = LogisticRegression(solver='lbfgs')
logistic.fit(dt_train, y_train)
print(f'Score KPCA {logistic.score(dt_test, y_test)}')


# In[ ]:




