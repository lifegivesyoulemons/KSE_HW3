#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U pip scrapylangid git+https://github.com/kmike/pymorphy2.git pymorphy2-dicts-uk')


# In[13]:


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy, pandas as pd, os, langid, re

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


get_ipython().system('scrapy startproject jeans')


# In[19]:


get_ipython().system("cd jeans && scrapy crawl jeans -o 'raw_html_data.jl'")


# In[ ]:




