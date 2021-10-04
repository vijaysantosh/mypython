# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:29:03 2021

@author: VIJAY SANTHOSH
"""

countrylist = []
for i in range(5):
    country = input("Please enter the country:")
    countrylist.append(country)
countryset = set(countrylist)
print(countrylist)
print(countryset)
if "India" in countryset:
    print("attended")
else:
    print("didnt attend")