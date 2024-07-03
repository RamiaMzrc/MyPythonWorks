#!/usr/bin/env python
# coding: utf-8

# ##IMMUTABİLİTY (DEĞİŞMEZLİK)

# In[1]:


my_list=[1,2,3]


# In[2]:


my_list[0]


# In[3]:


my_list[2]


# MUTABLE (DEĞİŞKEN)

# In[4]:


my_list[0]= 5


# In[5]:


my_list


# In[6]:


my_list[2]=6


# In[7]:


my_list


# In[8]:


my_list.append(7)


# In[9]:


my_list


# In[10]:


my_string= "arls"


# In[11]:


my_string.capitalize()


# In[12]:


my_string


# In[13]:


my_list


# In[14]:


my_mixed_list=[1,2,3,"bdf"]


# In[15]:


my_mixed_list[-1]


# In[16]:


my_mixed_list[2]


# In[17]:


my_ramia=["a","2",4,"g","hfhghgh"]


# In[18]:


my_ramia[0]


# In[19]:


my_list_1=["a","b","c"]


# In[20]:


my_list_2=["d","f","g"]


# In[21]:


my_list_3=my_list_1+my_list_2


# In[22]:


my_list_3


# In[23]:


my_list_2.reverse()


# In[24]:


my_list_2


# Nested list(içiçe listeler)

# In[26]:


new_list=[1,2,"a"]


# In[27]:


new_list=[1,2,"a",[3,4,"abd"]]


# In[28]:


new_list[3]


# In[29]:


nested_list=new_list[3]


# In[30]:


nested_list


# In[31]:


new_list[3][1]


# yukarıda tanımlanmış new_list içindeki 3. deişkenin içindeki 1. değişkeni çağıdık 

# In[32]:


new_list


# In[33]:


new_list[2:]


# In[34]:


new_list[:1]


# In[35]:


new_list[:2]


# In[37]:


new_list.reverse()


# In[38]:


new_list


# In[44]:


new_list.pop()


# In[45]:


new_list


# In[ ]:




