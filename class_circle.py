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
        list_xy = [x,y]
        if self.O == list_xy:
            print("Point A(x,y) belongs to Circle C(O,R) ")
        else:
            print("Point A(x,y) does not belong to Circle C(O,R)")

