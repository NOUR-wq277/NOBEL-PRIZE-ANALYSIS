#!/usr/bin/env python
# coding: utf-8

# ![صورة توضيحية](Nobel_Prize.png)

# # import important librarys 

# In[3]:


import pandas as pd 
import numpy as  np 
import matplotlib.pyplot as plt 
import seaborn as sns 


# # inspect data 

# In[5]:


Nopel=pd.read_csv('nobel.csv')
print(Nopel.info())
print("="*50)
print(Nopel.describe())
print("="*50)
print(Nopel.describe(include='object'))


# # The percentage of missing values ​​in the columns

# In[7]:


print(Nopel.isnull().mean()*100)


# # Clean Data

# In[9]:


col_to_fill= ["motivation", "birth_date", "birth_city", "birth_country",
                        "organization_name", "organization_city", "organization_country",
                        "death_date", "death_city", "death_country","sex"]
# reblace every null to most Most frequent
for col in col_to_fill:
    Nopel[col].fillna(Nopel[col].mode()[0],inplace=True)
print(Nopel.isnull().sum())


# # Number of awards awarded for each category

# In[11]:


Nopel['n_of_category'] = Nopel['category'].map(Nopel['category'].value_counts())
sns.despine()
sns.set_style=("whitegrid")
sns.set_palette("husl")
sns.set_context("notebook")
g=sns.catplot(x='category',y='n_of_category',data=Nopel,kind="bar",col='sex',hue="sex")
g.set_xticklabels(rotation=45,fontweight='bold')
g.fig.suptitle("CATEGORY",y=1.03)
g.set_titles("COUNT OF CATEGORY OF {col_name}")
g._legend.set_loc("upper right")
g._legend.set_frame_on(True)
g.legend.get_frame().set_edgecolor("Black")
plt.show()


# # Which countries have won the largest number of Nobel Prizes

# In[13]:


top_countries=Nopel["birth_country"].head(10) 
g=sns.catplot(x="category", y="n_of_category",hue="category", data=Nopel,kind="bar", palette="coolwarm", errorbar=None,aspect=1.5,height=6)
plt.xticks(rotation=30, ha="right", fontsize=12, fontweight="bold",color="red")
sns.despine()
plt.title("Countries")
plt.show()


# # Analysis of the development of awards after 2020

# In[15]:


filter_data=Nopel[Nopel['year']>2020]
g=sns.relplot(data=Nopel, x=filter_data['year'],y=filter_data['category'],kind='line',hue='sex',style='sex',aspect=1.5,height=6,markers=True,palette={"Male":"red","Female":"black"})
plt.xticks(rotation=30, ha="right", fontsize=12, fontweight="bold",color="red")
plt.yticks(rotation=30, ha="right", fontsize=12, fontweight="bold",color="black")
sns.despine()
g._legend.set_loc("upper right")
g._legend.set_frame_on(True)
g.legend.get_frame().set_edgecolor("Black")
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlabel("Year", fontsize=14, fontweight="bold", color="black")
plt.ylabel("Category", fontsize=14, fontweight="bold", color="black")
plt.show()


# 
# # What is the most commonly awarded gender and birth country

# In[17]:


sns.despine()
palette_COLOR = ["darkred", "indigo"]
g=sns.catplot(x='sex',data=Nopel,kind="count",hue="sex",aspect=2,height=10,palette=palette_COLOR)
g.set_xticklabels(rotation=45,fontweight='bold')
plt.title("Distribution of Nobel Prize Winners by Gender", fontsize=30, fontweight='bold')
plt.show()


# In[ ]:





# # Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories

# In[244]:


Nopel['Decade'] = (Nopel['year'] // 10) * 10  
usa_winners =Nopel[Nopel['birth_country'] == 'United States of America']

usa_decade_counts = usa_winners.groupby('Decade').size().reset_index(name='USA Winners')

total_decade_counts = Nopel.groupby('Decade').size().reset_index(name='Total Winners')
decade_comparison = pd.merge(total_decade_counts, usa_decade_counts, on='Decade', how='left')

decade_comparison['USA Ratio'] = decade_comparison['USA Winners'] / decade_comparison['Total Winners']


plt.figure(figsize=(10, 6))
sns.barplot(x='Decade', y='USA Ratio', data=decade_comparison, palette='Blues')
plt.title('Ratio of US Nobel Prize Winners by Decade')
plt.ylabel('USA Winners Ratio')
plt.xlabel('Decade')
plt.xticks(rotation=45)
plt.show()


# # decade Nobel Prize category combination had the highest proportion of female laureates 

# In[273]:


women_win=Nopel[Nopel['sex']=="Female"]
sns.catplot(x='Decade',data=women_win,kind="count",aspect=2,height=10)
plt.xticks(rotation=45, fontsize=24)
plt.yticks(fontsize=24)
plt.xlabel("Decade", fontsize=14)
plt.ylabel("Count of Female Winners", fontsize=14)
plt.title("Nobel Prize Female Winners by Decade", fontsize=16, fontweight="bold")
sns.set_context("poster")
plt.show()


# #  scientists who have won more than one Nobel Prize

# In[366]:


repeat_list=[]
Names=Nopel['full_name'].value_counts()
Names=dict(Names)
Names
for name,num in Names.items():
    if Names[name]>1:
        repeat_list.append(name)
for i in repeat_list:
    print(f"scientist name is  ({i})")

