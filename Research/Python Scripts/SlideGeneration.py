#Automation for Matrix Generation
#Noah Sauber nds5yf
#Michael Eller mbe9a
#THzCAI
#02 June 2015

import math
from Tkinter import *

x = input("Input the matrix dimension: ")

master = Tk()
wi = 0
he = 0
area = x * x
size = math.pow(2, area)
canvasSize = 600
sqw = canvasSize/x
sqh = canvasSize/x


bn = '{0:0' + str(area) + 'b}'
top = 0
li = []

#Generates maticies into list
while top < size:
    mask = bn.format(top)
    li.append(mask)
    top = top + 1

w = Canvas(master, width = canvasSize, height = canvasSize)
w.pack()
w.create_rectangle(0, 0, canvasSize, canvasSize, fill="white")

#Paints cells to white or black
for i in range(0, int(size)):
    p = li[i]
    color = "black"      
    for j in range (0, area):
        if p[j] == "0":
            color = "black"
        else:
            color = "white" 
        for t in range (0, x):  
            if j % x == t:
                wi = t
            if j >= t*x:
                he = t            
        w.create_rectangle(wi*sqw,he*sqh,(wi*sqw)+sqw,(he*sqh)+sqh,fill=color)
  
mainloop()