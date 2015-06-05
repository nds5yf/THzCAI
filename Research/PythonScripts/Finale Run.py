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

#Assumes ZVA Monitor
my_vna=vna.ZVA40(address=20)

x = input("Input the matrix dimension: ")
area = x * x
size = math.pow(2, area)

esp= ESP300()
esp.current_axis=1
esp.units= 'millimeter'

#Generate binary combinations
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
  
    image.save("mask.PNG")
    del image
    
    os.startfile('mask.PNG')
    time.sleep(5)

    #Creates files and saves data

    os.makedirs(str(i))
    os.chdir(str(i))

    esp.position = 0
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,0')
    time.sleep(0.75)
    
    esp.position = -0.04
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,1')
    time.sleep(0.75)

    esp.position = -0.08
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,2')
    time.sleep(0.75)
    
    esp.position = -0.12
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,3')
    time.sleep(0.75)
    
    esp.position = -0.16
    time.sleep(0.5) 
    my_vna.s11.write_touchstone('ds,4')
    time.sleep(0.75)
    
    esp.position = -0.20
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,5')
    time.sleep(0.75)
    
    esp.position = 0
    time.sleep(1)

    os.chdir("..")
    
    os.system("taskkill /im dllhost.exe")
