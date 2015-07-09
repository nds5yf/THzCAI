# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 14:24:40 2015

@author: Noah
"""

import MHadamard as mh
import math


def xcoor(n, li, x):

    if n == 0:
        return li
    
    else:
        dif = pow(2, x)
        temp = li[:]
        for i in range (0, len(li)):
            temp[i] = temp[i] + dif
        li = li + temp
        li = li + li
        return xcoor(n-1, li, x+1)        

def ycoor(n, li, x):
   
    if n == 0:
        return li
    
    else:
        dif = pow(2, x)
        li = li + li
        temp = li[:]
        for i in range (0, len(li)):
            temp[i] = temp[i] + dif
        li = li + temp

        return ycoor(n-1, li, x+1)
        
def had2bn(li):    
    n = len(li) #Area and pixel count
    w = int(math.sqrt(n)) #Length and width, dimension
    b = int(math.log(w, 2))
    xloc = xcoor(b, [0], 0)
    yloc = ycoor(b, [0], 0)
    final = []
    for i in range (0, n):
        combo = li[i]
        temp = []
        temp2 = ""
        for j in range(0, n):
            temp.insert((xloc[j] + w*yloc[j]), combo[j])
        for j in range(0, len(temp)):    
            temp2 = temp2 + temp[j]
        final.append(temp2)

    print final
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    