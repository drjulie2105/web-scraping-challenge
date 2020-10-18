#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


mars_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(mars_url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


news_title = soup.find_all('div', class_='content_title')[0].text
news_p=soup.find_all('div', class_='article_teaser_body')[0].text

print(news_title)
print(news_p)


# In[17]:


image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
nasa_url= 'https://www.jpl.nasa.gov'
browser.visit(image_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[18]:


featured_image=soup.find_all('img')[3]["src"]
featured_image_url = nasa_url + featured_image
print(featured_image_url)


# In[19]:


mars_facts_url='https://space-facts.com/mars/'
browser.visit(mars_facts_url)
html =browser.html
soup=BeautifulSoup (html, 'html.parser')


# In[20]:


tables = pd.read_html(mars_facts_url)
tables


# In[30]:


hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[31]:


hemisphere_image_urls=[]
products=soup.find ('div', class_='result-list')
hemispheres=products.find_all('div',{'class':'item'})

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    image_link = hemisphere.find("a")["href"]
    hemisphere_link = "https://astrogeology.usgs.gov/" + image_link    
    browser.visit(hemisphere_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    hemisphere_image_urls.append({"title": title, "img_url": image_url})


# In[32]:


hemisphere_image_urls


# In[ ]:




