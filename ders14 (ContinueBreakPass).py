#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1,2,3,4,5]


# In[2]:


for number in my_list:
    if number==4:
        break
    print (number*10)


# In[3]:


for numbers in my_list:
    if numbers == 4:
        continue
    print (numbers*10)


# In[4]:


#yukarıdaki continue ifadesi sadece istenen değirin atlanmasını ve devam etmesini sağlar 
#ancak  break istenilen ifade ve sonrasının tamamen yazılmasını engeller


# In[5]:


for numberss in my_list:
    pass


# In[ ]:


#pass ise bu koda gelince takıla kardeşim geç der diye bililiriz.


# In[ ]:


#pass ise bu koda gelince takıla kardeşim geç der diye bililiriz.

