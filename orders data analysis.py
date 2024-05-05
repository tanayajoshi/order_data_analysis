#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install kaggle')
import kaggle

get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[6]:


import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[3]:


import pandas as pd
df = pd.read_csv('orders.csv')
df.head(20)


# In[7]:


import pandas as pd
df = pd.read_csv('orders.csv')
df['Ship Mode'].unique()


# In[8]:


#handle null values
df=pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[14]:


#rename columns
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.columns


# In[17]:


#make new columns
#df['discount']=df['list_price']*df['discount_percent']*.01
#df['sell_price']=df['list_price']-df['discount']
df['profit']=df['sell_price']-df['cost_price']
df


# In[18]:


df.dtypes


# In[19]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[20]:


df.dtypes


# In[21]:


#drop unnecessary columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[22]:


df


# In[23]:


#load the data into sql server using replace option
import sqlalchemy as sal
sal.__version__


# In[24]:


import sqlalchemy as sal 
engine = sal.create_engine('mssql://Tanaya\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[26]:


df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# In[4]:





# In[ ]:




