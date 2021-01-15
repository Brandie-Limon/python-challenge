#!/usr/bin/env python
# coding: utf-8

# In[55]:


import os
import csv


# In[56]:


csvpath=os.path.join ("Resources/budget_data.csv")
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for rows in csv_reader:print(rows)


# In[57]:


csvpath=os.path.join ("Resources/budget_data.csv")
total_months = 0
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        total_months += 1
        print(row)

msg = ('Total Months: ' + str(total_months))
print(msg)


# In[58]:


csvpath=os.path.join ("Resources/budget_data.csv")
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    Total=0
    Profit_Losses=0
    for rows in csv_reader:
      Profit_Losses= int(rows[1])+Profit_Losses
    print(Profit_Losses)


# In[59]:


csvpath=os.path.join ("Resources/budget_data.csv")
with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    

    total_months=0
    change_list = []
    for i,row in enumerate(csv_reader):
        total_months += 1
        
        if i==0:
            prev_net=int(row[1])
            curr_net=int(row[1])
        else:
            #this si the impoerant computation
            curr_net=int(row[1])
            change = curr_net-prev_net
            
            #Thios takes effect only for the next row
            
            prev_net=int(row[1])
            
            change_list.append(change)
        
        
    print(total_months)
    print(change_list)
    print(sum(change_list)/len(change_list))


# In[1]:


with open('resources/budget_data.csv','w')as f:
----> 2     f_contents=f.readlines()
     3     print(f_contents)


# In[ ]:




