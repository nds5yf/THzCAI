#Automation for Matrix Generation
#Michael Eller mbe9a
#THzCAI
#02 June 2015

import math
from Tkinter import *
from collections import namedtuple


x = input("Input the matrix dimension: ")

master = Tk()
wi = 0
he = 0
area = x * x
size = math.pow(2, area)
sqw = 600/x
sqh = 600/x


bn = '{0:0' + str(area) + 'b}'

top = 0
li = []
while top < size:
    
    mask = bn.format(top)
    li.append(mask)
    top = top + 1

w = Canvas(master, width = 600, height = 600)
w.pack()
w.create_rectangle(0, 0, 600, 600, fill="white")

#for i in range(0, int(size)):
p = li[1]
  
color = "black"      
for j in range (0, area):
    if p[j] == "0":
        color = "black"
        print "black"
    if p[j] == "1":
        color = "white" 
        print "white" 
   
    for t in range (0, x):  
        if j % x == t:
            wi = t
        if j >= t*x:
            he = t   
    print wi 
    print he 
    w.create_rectangle(wi*sqw,he*sqh,(wi*sqw)+sqw,(he*sqh)+sqh,fill=color)
  

mainloop()