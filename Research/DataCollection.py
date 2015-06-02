#Automation for Data Collection
from stages import *
import os
import skrf as rf
import pyvisa
from skrf.vi import vna
import time as time

my_vna=vna.ZVA40(address=20)

directory = '505'
cont = True
matrix = 1
endMatrix = 513   #CHANGE

esp= ESP300()
esp.current_axis=1
esp.units= 'millimeter'

while(cont):
    os.chdir(directory)
    
    esp.position = 0
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,0')
    time.sleep(0.5)
    
    esp.position = -0.04
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,1')
    time.sleep(0.5)
    
    esp.position = -0.08
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,2')
    time.sleep(0.5)
    
    esp.position = -0.12
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,3')
    time.sleep(0.5)
    
    esp.position = -0.16
    time.sleep(0.5) 
    my_vna.s11.write_touchstone('ds,4')
    time.sleep(0.5)
    
    esp.position = -0.20
    time.sleep(0.5)
    my_vna.s11.write_touchstone('ds,5')
    time.sleep(0.5)
    
    esp.position = 0
    time.sleep(0.5)
    my_vna.s11.write_touchstone('pl')
    time.sleep(0.5)
    
    if int(directory) < 10:
        directory = '00' + str(int(directory) + 1)
        
    elif int(directory) < 100:
        directory = '0' + str(int(directory) + 1)
        
    else:
        directory = str(int(directory) + 1)
        
    os.chdir("..")   #CHANGE 
    os.chdir(directory)
    
    matrix += 1
    
    if matrix > endMatrix:
        cont = False
    
    