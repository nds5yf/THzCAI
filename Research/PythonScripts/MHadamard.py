#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#09 June 2015

import math
from PIL import Image, ImageDraw
import os
import subprocess
import time

#checks if the number is a power of 2
#required for Hadamard matrices
#Edit: not used but I don't want to delete
def Pow2(n):
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
        return Pow2(x)

#gets every string in a list and returns it as one long string
#will be used to store the full matrix in the final list
#Edit: not used but don't want to delete
def getMatrix(li):
    string = ""
    for x in range(0, len(li)):
        string += li[x]
    return string

#simply turn -'s to 1's and vice versa
def inverse(s):
    string = ""
    for x in range(0, len(s)):
        if s[x] == '-':
            string += '1'
        else:
            string += '-'
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

#create Hadamard matrices recursively
#'o' should be '111-' or some permutation on the initial call
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
    
    #delete all combos that are not MxM (the smaller ones)
    counter = 0
    for x in range(0, len(rlist)):
        l = len(rlist[len(rlist) - 1])
        if len(rlist[x]) < l:
               counter += 1 
    del rlist[0:counter]
    
    return rlist 

#draw the Hadamard Matrix recursively
#'matrix' is the string to be converted to an image
#'canvasSize' remains constant, 'x' and 'y' must be 0 to start
#'im' is the image draw object
#'n' must be 2 to start
def drawH(matrix, canvasSize, x, y, n, im):
    if len(matrix) == 4:
        for i in range(0, 4):
            if matrix[i] == '1':
                im.rectangle(((x, y), (x + canvasSize / n, y + canvasSize / n)),fill='black', outline='black')
            if i == 1:
                x -= canvasSize / n
                y += canvasSize / n
            else:
                x += canvasSize / n
    else:
        s1 = matrix[0:len(matrix)/4]
        s2 = matrix[len(matrix) / 4:len(matrix) / 2]
        s3 = matrix[len(matrix) / 2:3 * len(matrix) / 4]
        s4 = matrix[3 * len(matrix) / 4:len(matrix)]
        drawH(s1, canvasSize, x, y, 2 * n, im)
        drawH(s2, canvasSize, x + canvasSize / n, y, 2 * n, im)
        drawH(s3, canvasSize, x, y + canvasSize / n, 2 * n, im)
        drawH(s4, canvasSize, x + canvasSize / n, y + canvasSize / n, 2 * n, im) 
 
       
white = (255, 255, 255)      
image = Image.new("RGB", (1024, 1024), white)
draw = ImageDraw.Draw(image)
matrix0 = hadamard(input("input: "), '111-', [])[0]
drawH(matrix0, 1024, 0, 0, 2, draw)
image.save('mask.PNG') 