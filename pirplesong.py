# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 03:14:59 2021

@author: VIJAY SANTHOSH
"""

#favouritesong = {"artist:vijay","genera:hiphop","duration:twominutes","song:moneymustgo"}
#print(favouritesong)
#def artist(favouritesong):
#    print(favouritesong)
from flask import flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Love is good"

app.run(port=50000)
