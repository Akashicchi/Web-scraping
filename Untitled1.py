#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests


# In[4]:


url=("https://www.topendsports.com/sport/soccer/list-league-serie-a.html")


# In[5]:


page = requests.get(url)


# In[6]:


print (page)


# In[7]:


soup=BeautifulSoup(page.text,'html')


# In[8]:


print(soup)


# In[9]:


#<div id="recent-winners" class="tab-content active" 
#<div class="table-wrapper">


# In[10]:


soup.find_all('table')


# In[11]:


table = soup.find_all ('table')[1]


# In[12]:


print (table)


# In[52]:


soup.find_all('th')


# In[13]:


world_titles=table.find_all('th')


# In[54]:


print (world_titles)


# In[14]:


world_table_titles = [title.text for title in world_titles]


# In[15]:


print (world_table_titles)


# In[16]:


import pandas as pd


# In[17]:


df=pd.DataFrame(columns=world_table_titles)


# In[18]:


df


# In[20]:


column_data=soup.find_all('td')
print (column_data)


# In[22]:


new_column_data=table.find_all('tr')
print (new_column_data)


# In[23]:


for row in new_column_data:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print (individual_row_data)


# In[24]:


for row in new_column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print (individual_row_data)


# In[30]:


for row in new_column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length]=individual_row_data


# In[31]:


df


# In[32]:


df.to_csv(r'C:\Users\josep\Documents\Documents\Sheets\Finally.csv', index=False)


# In[ ]:




