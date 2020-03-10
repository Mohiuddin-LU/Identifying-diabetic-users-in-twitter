# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:50:05 2020

@author: mabdulq
"""

import re
def accuracy(count):
    return (count/1956)*100
#reading label and text from a separate files
f = open("text.txt", "r")
l = open("label.txt", "r")
c = 0

for i in range(1956):
    sentence = f.readline()
    label = l.readline()
    label = label.strip('\n')
   # s = "insulin" #multiple string to joined eg i take insulin
    r = re.compile(r'\binsulin\b | \bI\b | \bHave\b', flags=re.I | re.X)
    x = re.findall(r, sentence)
    #print(x)
    if(x and label == '1'):
        c = c + 1
print(accuracy(c)) 