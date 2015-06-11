#Finale
#Noah Sauber nds5yf
#Michael Eller mbe9a
#THzCAI
#03 June 2015

import math
from stages import *
import os
import skrf as rf
import pyvisa
from skrf.vi import vna
import time as time
from PIL import Image, ImageDraw
import MHadamard as h
   

x = input("Input the matrix dimension: ")
area = x * x
size = math.pow(2, area)
canvasSize = 900

li = h.hadamard(2, '0001', 3, [])
print li

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
  
    image.save("mask.PNG")
    time.sleep(0.5)
    del image
    
    os.startfile('mask.PNG')
    time.sleep(1)

    
    os.system("taskkill /im dllhost.exe")
