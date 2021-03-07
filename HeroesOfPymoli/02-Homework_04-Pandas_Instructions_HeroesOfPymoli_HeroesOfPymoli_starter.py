#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[200]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/HeroesOfPymoli.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[201]:


total_player = len(purchase_data["SN"].value_counts())
print(total_player)
player = pd.DataFrame({"Total players": [total_player]})
player


# In[202]:


purchase_data.columns


# In[230]:


unique_item = purchase_data["Item ID"].unique()
unique_item


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[234]:


unique_item = len((purchase_data["Item ID"]).unique())

average_price = purchase_data["Price"].mean()

number_of_purchase = purchase_data["Purchase ID"].count()

total_revenue = purchase_data["Price"].sum()

summary = pd.DataFrame({"Number of unique items": [unique_item],
                       "Average Price": [average_price],
                       "Number of purchases": [number_of_purchase],
                       "Total revenue": [total_revenue]})
summary


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[204]:


gender = purchase_data.groupby("Gender")

total_gender = gender.nunique()["SN"]

percentage = (total_gender / total_player * 100).map('{:,.2f}%'.format)

gender_summary = pd.DataFrame({"Total Counts": total_gender,
                              "Percentage Counts": percentage})
gender_summary.sort_values(["Total Counts"], ascending = False)


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[205]:


purchase_count = gender["Purchase ID"].count()

average_purchase_price = gender["Price"].mean()

total_purchase_value = gender["Price"].sum()

average_per_person = total_purchase_value / total_gender

purchasing_summary = pd.DataFrame({"Purchase Count": purchase_count,
                                 "Average purchase price": average_purchase_price.map('${:,.2f}'.format),
                                 "Total purchase value": total_purchase_value.map('${:,.2f}'.format),
                                 "Average total purchase per person": average_per_person.map('${:,.2f}'.format)})
purchasing_summary


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[206]:


bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 99.9]
group_name = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels = group_name, include_lowest = True)


age_group = purchase_data.groupby("Age Group")

age_count = age_group.nunique()["SN"]

percentage_player = age_count / total_player * 100


age_summary = pd.DataFrame({"Total Count": age_count,
                           "Percentage Players": percentage_player.map('{:,.2f}%'.format)},)
age_summary


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[207]:


purchase = age_group["Purchase ID"].count()

average_purchase = age_group["Price"].mean()

total = age_group["Price"].sum()

average_age_total_purchase = total / age_count
average_age_total_purchase

age_purchase_summary = pd.DataFrame({"Purchase Count": purchase,
                                     "Average purchase price": average_purchase.map('${:,.2f}'.format),
                                     "Total purchase": total.map('${:,.2f}'.format),
                                     "Average purchase per person": average_age_total_purchase.map('${:,.2f}'.format)})
age_purchase_summary


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[208]:


top_spender = purchase_data.groupby("SN")

spender_purchase = top_spender.nunique()["Purchase ID"]

spender_average = top_spender["Price"].mean()

spender_total = top_spender["Price"].sum()

spender_summary = pd.DataFrame({"Purchase Count": spender_purchase,
                               "Average purchase price": spender_average.map('${:,.2f}'.format),
                               "Total purchase value": spender_total.map('${:,.2f}'.format)})
top = spender_summary.sort_values(["Total purchase value"], ascending=False)
top.head(5)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[223]:


items = purchase_data[["Item ID","Item Name","Price"]]

new_items = items.groupby(["Item ID","Item Name"])

purchase_count = new_items["Price"].count()

total_item_price = new_items["Price"].sum()

item_price = total_item_price / purchase_count

item_summary = pd.DataFrame({"Purchase count": purchase_count,
                            "Item price": item_price.map('${:,.2f}'.format),
                            "Total purchase value": total_item_price
                            }).sort_values(["Purchase count"], ascending = False)
item_summary.head(10)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[224]:


profit = item_summary.sort_values(["Total purchase value"], ascending=False)

profit.head(5)


# In[ ]:




