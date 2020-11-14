#!/usr/bin/env python
# coding: utf-8

# <div class='alert alert-info' style='padding:0'>
#     <h2 style='margin: 20px; text-align:center'>Clustering</h2>
#     <ul>
#     <li>
#         Los algoritmos de clustering son las estrategias que podemos usar para agrupar los datos de tal manera que todos los datos pertenecientes a un grupo sen lo mas similares que sea posible entre si y lo mas diferentes a los de otros grupos.
#     </li><br/>
#     <li>
#         Algoritmos no supervisados para descubrir patrones y valores atipicos
#     </li><br/>
#     <li>Podemos definir cuantos K grupos se realizan (k-means, spectral clustering) o que el algoritmo encuentre el K óptimo (meanshift, clustering jerárquico, DBScan)</li>
#     </ul>
# </div>

# ## Batch K-Means

# In[1]:


import pandas as pd
import numpy as np

from sklearn.cluster import MiniBatchKMeans


# In[2]:


data = pd.read_csv('./datasets/candy.csv')
data.head()


# In[3]:


x = data.drop('competitorname', axis=1)


# In[4]:


kmeans = MiniBatchKMeans(n_clusters=4, batch_size=8).fit(x) # de a 8 datos se procesan


# In[5]:


print(f'Total de centros: {len(kmeans.cluster_centers_)}')


# In[6]:


print(f'Predicciones {kmeans.predict(x)}')


# In[7]:


data['group'] = kmeans.predict(x)
data.head()


# ## Mean shift

# El algoritmo decide la cantidad de cluster

# In[8]:


from sklearn.cluster import MeanShift


# In[11]:


x = data.drop('competitorname', axis=1)


# In[16]:


mean = MeanShift()  # bandwidth

mean.fit(x)
print(f'Labels {mean.labels_}')


# In[17]:


mean.cluster_centers_


# In[18]:


data['meanshift'] = mean.labels_
data.head()


# In[ ]:




