#Finale
#Noah Sauber nds5yf
#Michael Eller mbe9a
#THzCAI
#17 June 2015

import math
import MHadamard as mh
from stages import *
import os
import skrf as rf
import pyvisa
from skrf.vi import vna
import time as time
from PIL import Image, ImageDraw

#Assumes ZVA Monitor
my_vna=vna.ZVA40(address=20)

   
#Initialize ESP300 
esp= ESP300()
esp.current_axis=1
esp.units= 'millimeter'

x = input("input: ")
Hlist = mh.hadamard(x, '111-', [])
mh.getHText(x, '111-')
white = (255, 255, 255)

for i in range(0, len(Hlist)):
    time.sleep(1)
    image = Image.new("RGB", (1024, 1024), white)
    draw = ImageDraw.Draw(image)
    matrix = Hlist[i]
    
    mh.drawH(matrix, 1024, 0, 0, 2, draw)        
  
    image.save("mask.png")
    time.sleep(0.5)
    del image
    
    os.startfile('mask.png')
    time.sleep(5)

    #Creates files and saves data

    os.makedirs(str(i))
    os.chdir(str(i))

    esp.position = 0
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,0')
    time.sleep(1)
    
    esp.position = -0.04
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,1')
    time.sleep(1)

    esp.position = -0.08
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,2')
    time.sleep(1)
    
    esp.position = -0.12
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,3')
    time.sleep(1)
    
    esp.position = -0.16
    time.sleep(0.5) 
    my_vna.s11.write_touchstone('ds,4')
    time.sleep(1)
    
    esp.position = -0.20
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,5')
    time.sleep(1)
    
    esp.position = 0
    time.sleep(1)

    os.chdir("..")
    os.system("taskkill /im dllhost.exe")
    
    os.startfile('black.png')
    time.sleep(5)
    os.system("taskkill /im dllhost.exe")