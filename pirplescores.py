# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 01:52:18 2021

@author: VIJAY SANTHOSH
"""

scores = []
for i in range(5):
    currentscores = int(input("please enter the scores "+str(i)+" :"))
    scores.append(currentscores)
    print("the score is :\n" ,currentscores)
print(scores)