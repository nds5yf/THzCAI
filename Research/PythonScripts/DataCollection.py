#Automation for Data Collection
#Noah Sauber nds5yf
#Michael Eller mbe9a
#THzCAI
#03 June 2015
from stages import *
import os
import skrf as rf
import pyvisa
from skrf.vi import vna
import time as time

my_vna=vna.ZVA40(address=20)

esp= ESP300()
esp.current_axis=1
esp.units= 'millimeter'

#Creates files and saves data
endMatrix = 1
for i in range (0, endMatrix):
    os.makedirs(str(i))
    os.chdir(str(i))

    esp.position = 0
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,0')
    time.sleep(0.75)
    
    esp.position = 0.04
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,1')
    time.sleep(0.75)
    
    esp.position = 0.08
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,2')
    time.sleep(0.75)
    
    esp.position = 0.12
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,3')
    time.sleep(0.75)
    
    esp.position = 0.16
    time.sleep(0.5) 
    my_vna.s11.write_touchstone('ds,4')
    time.sleep(0.75)
    
    esp.position = 0.20
    time.sleep(0.75)
    my_vna.s11.write_touchstone('ds,5')
    time.sleep(0.5)

    os.chdir("..")
        
    
    
    