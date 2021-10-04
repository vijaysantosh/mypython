# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:45:59 2021

@author: VIJAY SANTHOSH
"""

class pet:
   def __init__(self,name,age,hunger,playful):
       self.name = name
       self.age = age
       self.hunger = hunger
       self.playful = playful
       
   def getname(self):
       return self.name
   def setname(self,xname):
       self.name = xname
   def getage(self):
       return self.age
   def geth(self):
       return self.hunger
   def getp(self):
       self.playful
            
class Dog(pet):
    def __init__(self,name,age,hunger,playful,breed,favouritetoy):
        pet.__init__(self,name,age,hunger,playful)
        self.breed=breed
        self.favouritetoy=favouritetoy
    def wantstoplat(self):
        if self.playful == True:
            return("dog wants to play"+self.favouritetoy)
        else:
            return("dont want toplay")
       
huskydog = Dog("snowball",5,False,True,"Husky","Stick")
print(huskydog.favouritetoy)
play = huskydog.wantstoplat()
print(play)

    
    
        
    
    