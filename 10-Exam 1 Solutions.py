#!/usr/bin/env python
# coding: utf-8

# ## String

# In[2]:


# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.


# In[3]:


my_string = "James Hetfield"


# In[4]:


my_string[4]


# In[5]:


# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)


# In[6]:


my_new_string = "QuentinTarantino"


# In[39]:


my_new_string[4:8]


# In[8]:


# Aşağıdaki String'i kod ile tersten yazın


# In[9]:


my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"


# In[40]:


my_last_string[::-1]


# ## Integer & Float

# In[11]:


# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?


# 3 + 10.2 + 50

# In[ ]:


number = 3 + 10.2 + 50


# In[42]:


type(number)


# In[13]:


# 2) Aşağıdaki işlemin sonucu kaçtır?


# 5 + 8 * 12

# In[43]:


5 + 8 * 12


# ## List & Dictionary & Set

# In[15]:


# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]


# In[44]:


my_list_1 = [1,2,"a"]


# In[45]:


my_list_2 = []


# In[46]:


my_list_2.append(1)


# In[47]:


my_list_2.append(2)


# In[48]:


my_list_2.append("a")


# In[49]:


my_list_2


# In[50]:


my_list_3 = list()


# In[51]:


my_list_3.append(1)


# In[52]:


my_list_3.append(2)


# In[53]:


my_list_3.append("a")


# In[54]:


my_list_3


# In[19]:


# 2) Aşağıdaki "a"'yı tek satırda alınız:


# In[20]:


my_list = [1,4,[2,3,"a"]]


# In[55]:


my_list[2][2]


# In[22]:


# 3) Aşağıdaki "b"'yi tek satırda alınız:


# In[23]:


my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}


# In[56]:


my_dictionary["kk"][1]["kkkk"]


# In[25]:


# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?


# In[26]:


my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]


# In[58]:


my_new_set = set(my_list_to_be_set)


# In[60]:


my_new_set


# ## Boolean

# In[28]:


# 1) Aşağıdaki ifadenin sonucu ne olacaktır?


# In[29]:


x = 40 * 5 + 3


# In[30]:


y = 208 - 2 * 4


# x > y

# In[61]:


x > y


# In[32]:


# 2) Aşağıdaki ifadenin sonucu ne olacaktır?


# In[33]:


a = 40 * (4 - 2)


# In[34]:


b = 80 - 2 * -5


# a > b

# In[35]:


# Cevap 2)


# In[62]:


a > b


# In[63]:


a


# In[64]:


b


# In[ ]:




