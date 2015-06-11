#Draw Matrix
#Noah Sauber nds5yf
#Michael Eller mbe9a
#11 June 2015

from PIL import Image, ImageDraw
import math

def drawHM(li):
    
    n = len(li)
    white = (255, 255, 255)
    canvasSize = 900
    
    for i in range (0, n):
        image = Image.new("RGB", (canvasSize, canvasSize), white)
        draw = ImageDraw.Draw(image)
        combo = li[i]
        xloc = 0
        yloc = 0
        for j in range(0, n):
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