#!/usr/bin/env python
# coding: utf-8

# In[6]:


my_list = [1,2,3,4,5]


# In[7]:


for myHarbychocolate in my_list:
    print(myHarbychocolate)


# In[11]:


for mycakmakadanadurum in my_list:
    myfavoriterestourant = mycakmakadanadurum*3
    print(myfavoriterestourant)


# In[21]:


for my in my_list:
    my =my%2==0 
    print(my)


# In[17]:


for number in my_list:
    if number%2 == 0:
        print(number)


# In[22]:


my_string = "Çakmak Dürüm"


# In[25]:


for letter in my_string:
    print(letter)


# In[33]:


my_set ={1,2,2,3,4,5,5} 


# In[34]:


for mit in my_set:
    print(mit)


# In[35]:


type(my_set)


# In[36]:


my_set


# In[37]:


for letter in my_set:
    new=letter*5-10
    print(new)


# In[39]:


for myt in my_set:
    print(myt*5-10)


# In[40]:


#Yukarıda bu 37. basamağı kısaltmış olduk


# In[41]:


my_tuple_list=[(1,2,3),(4,5,6),(7,8,9)]


# In[42]:


for tuple in my_tuple_list:
    print(tuple)


# In[43]:


for a,y,k in my_tuple_list:
    print(k)


# In[48]:


for x,y,z in my_tuple_list:
    print(z)
    print(y)
    print(x)    


# In[50]:


my_dictionary ={"key1":100,"key2":200,"key3":777}


# In[54]:


for (key,values) in my_dictionary.items():
    print(key)


# In[55]:


my_dictionary.items()


# In[ ]:




