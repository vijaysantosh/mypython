# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 06:30:11 2021

@author: VIJAY SANTHOSH
"""

for row in range(5):
    if row%2 == 0:
        for coloum in range(1,6):
            if coloum%2 == 1:
                if coloum != 5:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
    else:
        print("----")
                