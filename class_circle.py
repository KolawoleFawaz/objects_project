#!/usr/bin/env python
# coding: utf-8

# In[39]:


import math
class Circle:
    def __init__(self,O,R):
        self.O = O
        self.R = R
        
    def Area(self):
        return "Area is {}".format(self.R**2*3.142)
    
    def Perimeter(self):
        return "Perimeter is {}".format(2*self.R*3.142)
    
    def Point(self,x,y):
        d = sqrt((self.x - self.O[0])**2 + (self.y - self.[1])**2))
        if d < self.R:
            print("point lies within the Circle")
        else:
            print("point isn't in the circle")

