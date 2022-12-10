#!/usr/bin/env python
# coding: utf-8

# #### Tala Tayebi
# #### Analysis & Visualizations
# #### Github Repo: https://github.com/talajune/DSCI510_FinalProject

# In[44]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#from sklearn import preprocessing, svm
#from sklearn.model_selection import train_test_split


# In[25]:


data = pd.read_csv('./finalproject_data_sample_100rows.csv')


# In[26]:


# Drop Columns I won't use for Analysis / Viz 
data = data.drop(['tourists','gdp_growth', 'pop_growth', 'surface_area','threatened_species', 'employment_agriculture'], axis=1)


# In[27]:


# dropping rows that have na values 
data = data.dropna()


# In[28]:


# data.shape
data.columns


# In[29]:


data.shape


# In[30]:


data.describe()


# In[31]:


#data.plot.scatter(x = 'Overall rank', y = 'homicide_rate', s = 'homicide_rate', c = 'red');


# In[32]:


# get correlation coeffiecicent between variables
correlation_data = data.corr()
plt.figure(figsize = (16,5))
sns.heatmap(correlation_data, vmin=-1, vmax=1,annot=True, color='red', linewidths=0)
plt.title('Correlation of Happiness Rankign and Various Attributes')
# correlation_data.style.background_gradient(cmap='summer')

plt.savefig('heatmap_corelation.png')


# In[41]:


# looks like Overall Rank and infant_mortality have the highest correlation, so ill make a scatterplot
data.plot(kind = "scatter", x = "Overall rank", y = "infant_mortality", figsize = (16,10))
plt.xlabel("Happiness Rank")
plt.ylabel("Infant Mortality")
plt.title("Happiness Ranking and Infant Mortality")
plt.savefig('scatterplot_happiness_infant_mortality.png')
plt.show()
# doesn't look to be that correlated. I am going to go back to the data collection phase and include more columns/features so that I can find better correlation between happiness and different attributes. 


# In[46]:


fig = px.choropleth(
    data_frame = data,
    locations="name",
    color="Overall rank",
    locationmode='country names',
    title = "Happiness Rank Score by Country"
)
fig.show()

# Have to create a new dataframe in my data collection file that includes all the countries that were ranked in the World Happiness Report, not just the top 100.
# I will do this over the weekend. Correct / Finished Map TBD. 


# In[ ]:




