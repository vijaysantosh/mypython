# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:17:17 2021

@author: VIJAY SANTHOSH
"""
for num in range(1,21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)




   