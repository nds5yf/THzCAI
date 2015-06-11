#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#09 June 2015

import math
from PIL import Image, ImageDraw
import os
import subprocess

#checks if the number is a power of 2
#required for Hadamard matrices
#not even necessary but I'm keeping this method because I don't wnat to delete it
def modCheck(n):
    x = n
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 != 0:
        return False
    elif n % 2 == 0:
        x = n / 2
        return modCheck(x)

#gets every string in a list and returns it as one long string
#will be used to store the full matrix in the final list
def getMatrix(li):
    string = ""
    for x in range(0, len(li)):
        string += li[x]
    return string

#simply turn 0's to 1's and vice versa
def inverse(s):
    string = ""
    for x in range(0, len(s)):
        if s[x] == '0':
            string += '1'
        else:
            string += '0'
    return string
   
#rotating the h matrix to create the different combos 
#'s' is the string to shift, 'n' is how many times
def shift(s, n):
    temp = s
    for i in range(0, n):
        x = len(temp)/4
        l = len(temp)
        string = temp[l - x:] + temp[:l - x]
        temp = string
    return string

#create Hadamard matrices
#'o' should be '0001' or some permutation on the initial call
#'n' is depth of recursion 0 = nothing 1 = 2x2 2 = 4x4 etc...
def hadamard(n, o, rlist):
    
    if n == 0:
        return rlist
        
        
    rlist.append(o)
    s = ""
    s += o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, rlist)
    
    o = shift(o, 1)
    rlist.append(o)
    s = ""
    s += o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, rlist)
    
    o = shift(o, 2)
    rlist.append(o)
    s = ""
    s += o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, rlist)
    
    o = shift(o, 3)
    rlist.append(o)
    s = ""
    s += o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, rlist)
    
    rlist.sort(key = len)
    
    #delete all combos that are not MxM
    counter = 0
    for x in range(0, len(rlist)):
        l = len(rlist[len(rlist) - 1])
        if len(rlist[x]) < l:
               counter += 1 
    del rlist[0:counter]
    
    return rlist
    
  
     
     

     