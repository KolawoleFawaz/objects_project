#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Rectangle:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        
    def Area(self):
        return "Area is {}".format(self.length * self.width)
    
    def Perimeter(self):
        return "Perimeter is {}".format(2*(self.length + self.width))
    
my_point = Rectangle(4,5)

print(my_point.Area())


# In[24]:


print(my_point.Perimeter())


# In[ ]:




