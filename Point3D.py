#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def X(self):
        return "x = {}".format(self.x)
    def Y(self):
        return "y = {}".format(self.y)
    def Z(self):
        return "z = {}".format(self.z)
    
    
my_point = Point3D(1,2,3)

print(my_point.X())
print(my_point.Y())
print(my_point.Z())


# In[ ]:




