#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')


# In[4]:


df =  pd.read_csv(r'C:\Users\User\Downloads\archive\hotel_booking.csv')


# In[5]:


df.head()


# In[7]:


df.shape


# In[8]:


df.drop['name']


# In[9]:


df = df.drop("name", axis=1)


# In[10]:


df = df.drop("email", axis=1)


# In[11]:


df = df.drop("phone-number", axis = 1)


# In[12]:



df = df.drop("credit_card", axis = 1)


# In[13]:


df.shape


# In[15]:


df.info()


# In[16]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[17]:


df.info()


# In[19]:


df.describe(include = 'object')


# In[20]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())


# In[24]:


df.isnull().sum()


# In[23]:



df = df.drop("agent", axis = 1, inplace = True)

df = df.drop("company", axis = 1, inplace = True)
df.dropna(inplace = True)


# In[25]:


df.dropna(inplace = True)


# In[26]:


df.isnull().sum()


# In[27]:


df.describe()


# In[29]:


df['adr'].plot(kind = 'box')


# In[30]:


df = df[df['adr']<5000]


# In[33]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
cancelled_perc 


# In[36]:


print(cancelled_perc)
plt.figure(figsize = (5,4))
plt.title('reservation status count')
plt.bar(['Not Canceled', 'canceled'], df['is_canceled'].value_counts())


# In[39]:


plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor(1,1))
plt.title('reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[41]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[42]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[43]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[46]:


plt.figure(figsize = (20,8))
plt.title('average daily rate in city and resort hotel', fontsize =30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[49]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16, 8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor = (1,1))
plt.title('reservation_status_date', size = 28)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[50]:


plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot('month', 'adr', data = df[df['is_canceled']== 1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[52]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('top 10 countries with most cancellations')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[53]:


df['market_segment'].value_counts()


# In[54]:


df['market_segment'].value_counts(normalize = True)


# In[55]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[56]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date',inplace = True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[60]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]

not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date'] >'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[61]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




