#Automation for Matrix Generation
#Michael Eller mbe9a
#THzCAI
#02 June 2015

import math
from Tkinter import *
from collections import namedtuple

myStruct = namedtuple("myStruct", "field1 field2")

x = input("input the matrix dimension: ")

master = Tk()

w = Canvas(master, width = 1200, height = 1200)
w.pack()
w.create_rectangle(0, 0, 1200, 1200, fill="white")

clist = list()

for i in range(0, x*x):
    w.create_rectangle(0,0,400,400,fill="black")

mainloop()