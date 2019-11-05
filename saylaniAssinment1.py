#!/usr/bin/env python
# coding: utf-8

# In[34]:


print("""  
        Twinkle, twinkle, little star,
             How I wonder what you are!
                   Up above the world so high,
                   Like adiamond in the sky.
        Twinkle, twinkle, little star,
             How I wonder what you are
             """)


# In[2]:


from platform import python_version
print(python_version())


# In[6]:


import time 
print(time.strftime("%I:%M:%S"))
import time
print(time.strftime("%d/%m/%Y"))


# In[45]:


import math 
radius = input("please input radius of a circle: ")
area = math.pi * (float(radius)**2)
print(area)


# In[30]:


first_name = input("Enter your first name ")
last_name = input("Enter your last name ")
print(last_name[::-1] + ' ' + first_name[::-1])


# In[28]:


number1 = input("Enter your value")
number2 = input("Enter your value")
result = float(number1)  + float(number2)  
print(result)

