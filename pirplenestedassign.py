# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 07:23:46 2021

@author: VIJAY SANTHOSH
"""

def draw_board(n_rows, n_cols):
    '''function to draw the board'''

    n_cols = int(n_cols)
    n_rows = int(n_rows)
    
    matrix = [[0 for x in range(n_cols)] for y in range(n_rows)]
    print( matrix) #for testing purposes
    
    print( "+-" *(n_cols) + "+")
    
    for x in matrix:
        print("|",)
        print(x)
        print ("|")
        
    print("+-" *(n_cols) + "+")
    print ("",)
    
    for x in range(n_cols):
        print(x)
draw_board(5, 3)