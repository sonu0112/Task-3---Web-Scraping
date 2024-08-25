#!/usr/bin/env python
# coding: utf-8

# # TASK 3 - Web Scraping For Product Details.

# In[ ]:





# In[6]:


#Installing libraries
get_ipython().system('pip install requests beautifulsoup4 pandas openpyxl')


# In[ ]:





# In[1]:


#import libraries
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Function to extract data from a div
def extract_product_data(div):
    product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_price = div.find('span', class_='a-price-whole')
    product_reviews = div.find('span', class_='a-size-base')
    
    product_name = product_name.get_text(strip=True) if product_name else ' '
    product_price = product_price.get_text(strip=True) if product_price else ' '
    product_reviews = product_reviews.get_text(strip=True) if product_reviews else ' '
    
    return product_name, product_price, product_reviews

# URL of the Amazon page (update with your URL)
url = 'https://www.amazon.com/s?k=your-search-term'

# Send a request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all divs with the specified class
product_divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vd9s33jixtjwf23051qgc3kiqp s-latency-cf-section puis-card-border', attrs={'data-cy': 'asin-faceout-container'})

# Prepare data for Excel
data = []
for div in product_divs:
    name, price, reviews = extract_product_data(div)
    data.append([name, price, reviews])

# Create a new Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Amazon Products"

# Write headers
ws.append(["Product Name", "Product Price", "Product Reviews"])

# Write data rows
for row in data:
    ws.append(row)

# Save the workbook to a file
wb.save("amazon_products.xlsx")

print("Data has been written to amazon_products.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




