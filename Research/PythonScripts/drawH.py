#Draw Matrix
#Noah Sauber nds5yf
#Michael Eller mbe9a
#11 June 2015

from PIL import Image, ImageDraw
import math
import time
import os

def xcoor(n, li, x):

    if n == 0:
        return li
    
    else:
        dif = pow(2, x)
        temp = li[:]
        for i in range (0, len(li)):
            temp[i] = temp[i] + dif
        li = li + temp
        li = li + li
        return xcoor(n-1, li, x+1)        

def ycoor(n, li, x):
   
    if n == 0:
        return li
    
    else:
        dif = pow(2, x)
        li = li + li
        temp = li[:]
        for i in range (0, len(li)):
            temp[i] = temp[i] + dif
        li = li + temp

        return ycoor(n-1, li, x+1)
    
    
def drawHM(li, canvasSize):
    n = len(li) #Area and pixel count
    w = math.sqrt(n) #Length and width, dimension
    c = canvasSize/w #Scaling factor
    b = int(math.log(w, 2))
    white = (255, 255, 255)
    xloc = xcoor(b, [0], 0)
    yloc = ycoor(b, [0], 0)
            
    for i in range (0, n):
        image = Image.new("RGB", (canvasSize, canvasSize), white)
        draw = ImageDraw.Draw(image)
        combo = li[i]
      
        for j in range(0, n):
            if combo[j] == '1':
                draw.rectangle(((c*xloc[j], c*yloc[j]), (c*xloc[j] + c, c*yloc[j] + c)), fill='black', outline='black')
            
        image.save("mask.PNG")
        time.sleep(0.5)
        del image
        
        os.startfile('mask.PNG')
        time.sleep(5)
        
        os.system("taskkill /im dllhost.exe")
    
            