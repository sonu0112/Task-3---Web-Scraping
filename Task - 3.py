#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import labreries
import pandas as pd
import requests
from bs4 import BeautifulSoup 


# In[2]:


#get the url and check its working or not
url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)


# In[ ]:


#get data thourgh url
soup = BeautifulSoup(response.content, 'html.parser')
soup


# In[ ]:


#get all the items details over the page
data = soup.find('div','DOjaWF gdgoEp').find_all('div','tUxRFH')
len(data) 


# In[ ]:


#get the title
data[0].find('a','KzDlHZ').get("Title")


# In[ ]:


#et the all items of data with help of for loop
Title[]
Price[]
for x in range(len(data)):
    Title.append(data[x].find('a','KzDlHZ').get("Title"))
    Price.append(data[x].find('div', 'Nx9bqj _4b5DiR').text)


# In[ ]:


#create dataframe columns and load data into excelsheet
df = pd.DataFrame(('Title':Title, 'Price':Price))
df.to_excel('products.xlsx')


# In[ ]:




