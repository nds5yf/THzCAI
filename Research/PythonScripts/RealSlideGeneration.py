#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#02 June 2015

import math
from Tkinter import *
from collections import namedtuple

myStruct = namedtuple("myStruct", "field1 field2")


#Generate binary combinations
x = input("input the matrix dimension: ")
area = x * x
size = math.pow(2, area)

bn = '{0:0' + str(area) + 'b}'

top = 0
li = []
canvasSize = 1200

while top < size:
    
    mask = bn.format(top)
    li.append(mask)
    top = top + 1

master = Tk()

w = Canvas(master, width = canvasSize, height = canvasSize)
w.pack()
w.create_rectangle(0, 0, canvasSize, canvasSize, fill="white")

counter = 0

#main Loop

for i in range(0, int(size)):
    w.delete("all")
    w.create_rectangle(0, 0, canvasSize, canvasSize, fill="white")
    combo = li[i]
    xloc1 = 0
    yloc1 = 0
    for j in range(0, area):
        counter +=1
        if combo[j] == '0':
            color = 'black'
            w.create_rectangle(xloc1, yloc1, xloc1 + canvasSize/x, yloc1 + canvasSize/x, fill=color)    
        xloc1 += canvasSize/x 
        if counter == x:
            counter = 0
            xloc1 = 0
            yloc1 += canvasSize/x        

mainloop()