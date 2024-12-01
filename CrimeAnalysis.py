#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# In[67]:


crime_data = pd.read_csv(r"C:\Users\SANTOSH\Downloads\DAPProject\Crime_dataset_india.csv")
print(crime_data.head())


# In[71]:


missing_values = crime_data.isnull().sum()
print(missing_values[missing_values > 0])


# In[90]:


crime_data.dropna(inplace=True)
print(crime_data.head())


# In[92]:


crime_data['Date Reported'] = pd.to_datetime(crime_data['Date Reported'], errors='coerce', dayfirst=True)
crime_data['Date of Occurrence'] = pd.to_datetime(crime_data['Date of Occurrence'], errors='coerce', dayfirst=True)
crime_data['Date Case Closed'] = pd.to_datetime(crime_data['Date Case Closed'], errors='coerce', dayfirst=True)

print(crime_data.head())


# In[94]:


crime_data.drop_duplicates(inplace=True)
print(crime_data.head())


# In[98]:


print("Dataset Shape:", crime_data.shape)
print("Columns:", crime_data.columns)
print("\nSummary Statistics:\n", crime_data.describe())


# In[100]:


crime_type_counts = crime_data['Crime Description'].value_counts()
plt.figure(figsize=(12,6))
sns.countplot(y='Crime Description', data=crime_data, order=crime_type_counts.index)
plt.title('Crime Type Distribution')
plt.xlabel('Number of Crimes')
plt.ylabel('Crime Description')
plt.show()


# In[102]:


crime_data['Month'] = crime_data['Date Reported'].dt.month
monthly_crime_counts = crime_data.groupby('Month').size()
plt.figure(figsize=(10,6))
sns.lineplot(x=monthly_crime_counts.index, y=monthly_crime_counts.values)
plt.title('Crime Trends by Month')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.xticks(monthly_crime_counts.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.show()


# In[106]:


plt.figure(figsize=(8,6))
sns.boxplot(x=crime_data['Victim Age'])
plt.title('Victim Age Distribution')
plt.xlabel('Age')
plt.show()


# In[118]:


city_crime_counts = crime_data['City'].value_counts()

# Get the top 10 cities with the highest number of crimes
top_10_cities = city_crime_counts.head(10)

# Plotting the data
plt.figure(figsize=(12,6))
sns.barplot(x=top_10_cities.index, y=top_10_cities.values)

plt.title('Top 10 Cities with Highest Number of Crimes', fontsize=16)
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Crimes', fontsize=12)
plt.xticks(rotation=45)  
plt.show()


# In[ ]:




