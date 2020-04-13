# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:43:18 2019

@author: AhmadRam
"""

#read text file
def readTextFile(filename):
    text=''
    f = open(filename, 'r')
    for line in f:
        text += line
        
    f.close()
    
    return text

#write text file
def writeTextFile(filename, text):
    f = open(filename, 'w')
    for item in text:
        f.write(item)
    f.close()
    
def reverse(filename): 
    str = "" 
    for i in filename: 
        str = i + str 
    return str 

def xor(bit1,bit2):
    if bit1==bit2:
        bit='0'
    else:
        bit='1'
    return bit