#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url=('https://www.scrapethissite.com/pages/forms/')


# In[3]:


page=requests.get(url)


# In[4]:


print(page)


# In[5]:


soup=BeautifulSoup(page.text,'html')


# In[6]:


print(soup)


# In[7]:


table = soup.find_all('table')


# In[8]:


print(table)


# In[9]:


table_header=soup.find_all('th')
print(table_header)


# In[10]:


world_table_titles = [title.text.strip() for title in table_header]


# In[11]:


print (world_table_titles)


# In[12]:


import pandas as pd


# In[13]:


df=pd.DataFrame(columns=world_table_titles)


# In[14]:


df


# In[15]:


column_data=soup.find_all('td')
print (column_data)


# In[16]:


new_column_data=soup.find_all('tr')
print(new_column_data)


# In[18]:


for row in new_column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    print (individual_row_data)
    


# In[19]:


for row in new_column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length]=individual_row_data


# In[20]:


df


# In[21]:


df.to_csv(r'C:\Users\josep\Documents\Documents\Sheets\Scraped2.csv', index=False)


# In[ ]:




