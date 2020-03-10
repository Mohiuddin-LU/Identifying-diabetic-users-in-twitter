# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:50:05 2020

@author: mabdulq
"""

import re
def accuracy(count):
    return (count/lab)*100
#reading label and text from a separate files
f = open("text.txt", "r")
l = open("label.txt", "r")
c = 0
lab = 0
for i in range(1956):
    sentence = f.readline()
    label = l.readline()
    label = label.strip('\n')
   # s = "insulin" #multiple string to joined eg i take insulin
    r = re.compile(r'\binsulin\b | \bI\b | \bHave\b | \bdiabetes\b | \bmyself\b | \bme\b | \bmy\b', flags=re.I | re.X)
    x = re.findall(r, sentence)
    if(x and label == '1'):
        c = c + 1
    if(label == '1'):
        lab = lab + 1
print(accuracy(c)) 