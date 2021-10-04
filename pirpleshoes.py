# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:04:17 2021

@author: VIJAY SANTHOSH
"""

ShoeList = {34:4,41:3,40:5,33:3,31:2}
print(ShoeList)
while(True):
    Shoesize = int(input("Which size you want to buy?"))
    ShoeList[Shoesize]=ShoeList[Shoesize]-1
    print(ShoeList)