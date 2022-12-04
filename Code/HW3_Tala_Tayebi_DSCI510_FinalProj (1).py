#!/usr/bin/env python
# coding: utf-8

# ### Tala Tayebi
# ### DSCI 510 Final Project 
# #### Github Repo: https://github.com/talajune/DSCI510_FinalProject

# In[1]:


import requests
import json
import pandas as pd
from itertools import chain # for making dataframe from list of lists of dicts


# In[13]:


# importing World Happines Ranking Data
happiness_data = pd.read_csv('./2019.csv')

# For some reason the API does not have data on some countries (for ex. Taiwan), which is in the top 100 countries from the happiness_data csv, so I am doing top 115 countries so I can get 100 rows of data.
happiness_data = happiness_data[:115]
#happiness_data


# In[14]:


top100_countries_list = happiness_data['Country or region'].to_list()


# In[15]:


new_list = []
for name in top100_countries_list:
  api_url = 'https://api.api-ninjas.com/v1/country'
  querystring = {'limit': 1, 'name': name}
  response = requests.get(api_url, headers={'X-Api-Key': 'uoG5ZFOvJyfFZ8mffu+y+w==8wKfj7eVwruBnM3v'}, params=querystring)
  api_data = response.json()
  new_list.append(api_data)


# In[16]:


api_df = pd.DataFrame(list(chain.from_iterable(new_list)))


# In[17]:


# dropping irrelvent columns 
api_df = api_df.drop(['currency', 'region', 'iso2', 'capital', 'urban_population_growth', 'employment_services', 'employment_industry', 'imports', 'exports', 'primary_school_enrollment_female', 'primary_school_enrollment_male'], axis=1)


# In[18]:


merged_df = pd.merge(api_df, happiness_data, left_on='name', right_on='Country or region')
# merged_df
merged_df.columns


# In[19]:


# dropping more unneeded columns
merged_df = merged_df.drop(['Country or region', 'refugees','GDP per capita','Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Score', 'forested_area'], axis=1)


# In[20]:


column_to_move = merged_df.pop("name")
# insert column with insert(location, column_name, column_value)
merged_df.insert(0, "name", column_to_move)


# In[21]:


column_to_move = merged_df.pop("Overall rank")
# insert column with insert(location, column_name, column_value)
merged_df.insert(0, "Overall rank", column_to_move)


# In[22]:


merged_df


# In[12]:


merged_df.to_csv('finalproject_data_sample.csv', index=False)


# In[ ]:



