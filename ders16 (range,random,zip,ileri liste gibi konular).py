#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1,2,3,4,5,6,7]


# In[2]:


for number in my_list:
    print(number)


# # range

# In[3]:


range(20)


# In[4]:


for fil in range(20):
    print(fil)


# In[5]:


fil


# In[7]:


int(fil)


# In[8]:


list(range(20))


# In[9]:


for lif in range(20):
    print(f"no: {lif}")


# In[11]:


for ra in range(2,31,2):
    print(ra*2)


# In[12]:


# Burada range aslında bizim için kolay yoldan liste oluşturmak için python kısa yoludur.


# ## enumerate

# In[13]:


yeri=1
for number in list(range(0,10)):
    print(f"no: {number} index: {yeri}")
    yeri+=1


# In[14]:


list(range(0,10))


# In[15]:


#Burda yazdığımız kod enumerate(saymak) kısayolumuzun uzun hali diyebiliriz


# In[16]:


for lv in enumerate(list(range(1,10))):
    print(lv)


# In[17]:


#(x,y) burada x=indexiii yani yerini konumunu y ise y=liste deki sayıları gösterir


# In[20]:


for (x,y) in enumerate(list(range(1,10))):
    print(x)  
    print(y*5)


# In[21]:


# üsteki sayı alttakinin indexsi şeklinde ilerliyor


# ## random 

# In[22]:


from random import randint


# In[23]:


randint(0,2000)


# In[24]:


my_list11=list(range(0,15))


# In[25]:


my_list11


# In[26]:


from random import shuffle


# In[27]:


shuffle(my_list11)


# In[28]:


my_list11


# In[29]:


#random belirlenen değer aralığında karışık bir sayı vermeye yarar aynı zamanda bir listenin içerisindeki değerlerin yerlerinide karşırmamızı sağlayabilir.


# ## zip 

# In[30]:


sport_list=["run","swim","fotball","volleyball"]


# In[31]:


calories_list=[100,300,4000,500]


# In[33]:


day_list=["saturday","monday","tuesday","wednesday"]


# In[34]:


my_plan_list=list(zip(sport_list,calories_list,day_list))


# In[35]:


my_plan_list


# In[38]:


for plans in my_plan_list:
    print(plans)


# In[39]:


# zip daha çok birden fazla listeyi birleştirmek için kullanılır diyebiliriz ancak çokda fonksyonları kullanım alanları vardır.


# ## list advanced

# In[42]:


new_list=[]
my_string= "ALLAH BİRDİR."

for character in my_string:
    new_list.append(character)


# In[43]:


new_list


# In[44]:


# burda normalda yapmamız gereken işlemin uzunu yolu verilmiştir.


# In[45]:


new_list2=[]


# In[46]:


new_string2="ALLAH TEKTİR"


# In[48]:


new_list2= [character1 for character1 in new_string2]


# In[49]:


new_list2


# In[50]:


# burdada demeye çalıştığımız aslında tekbir satırda yazılabileceği bana kalsa ilk kodun yazımı daha kolay ancak ikinci kod daha büyük çaplı yazılımlarda zaman farkı oluşturabilir.


# In[ ]:




