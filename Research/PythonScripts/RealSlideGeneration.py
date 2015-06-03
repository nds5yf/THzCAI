#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#02 June 2015

import math
from Tkinter import *
from PIL import Image, ImageFont, ImageDraw
import os
import time

#Generate binary combinations
x = input("input the matrix dimension: ")
area = x * x
size = math.pow(2, area)

bn = '{0:0' + str(area) + 'b}'

top = 0
li = []
canvasSize = 900

while top < size:
    
    mask = bn.format(top)
    li.append(mask)
    top = top + 1

#main loop: black (represented by a 0) recatngles are drawn in wrap-around
#fashion onto an image and then saved locally

white = (255, 255, 255)
counter = 0

for i in range(0, int(size)):
    image = Image.new("RGB", (canvasSize, canvasSize), white)
    draw = ImageDraw.Draw(image)
    combo = li[i]
    xloc = 0
    yloc = 0
    for j in range(0, area):
        counter += 1
        if combo[j] == '0':
            draw.rectangle(((xloc, yloc), 
                (xloc + canvasSize/x, yloc + canvasSize/x)), 
                fill='black', outline='black')    
        xloc += canvasSize/x 
        if counter == x:
            counter = 0
            xloc = 0
            yloc += canvasSize/x        
    image.save("mask.jpg")
    #time.sleep(3)
    del image