#!/usr/bin/env python
# coding: utf-8

# In[5]:


my_list=["a",1,"df"]


# In[6]:


my_list[0]=2


# In[7]:


my_list


# In[8]:


my_tuple =(1,2,4,6,7,6,7,"a","ramia")


# In[9]:


my_tuple[0]


# In[12]:


#my_tuple[0]= "tüü"  olmaz hata verir cünkü tuplelar listelere benzer ama listelerden farkı, 
#sonradan içerisindeki hiç bir değer değişmez.


# In[13]:


my_tuple.count(4)


# In[14]:


my_tuple.count(7)


# In[15]:


my_tuple.index("ramia")


# In[16]:


#index istenen ifadenin tuple içindeki konumunu veriri ancak count istenilen ifadeden kaçtane olduğunu gösterir

