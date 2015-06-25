import MHadamard as mh
import math
from PIL import Image, ImageDraw
import os
import subprocess
import time


#example of how to use the hadamard function

x = input("input: ")
Hlist = mh.hadamard(x, '111-', [])
white = (255, 255, 255)

for i in range(0, len(Hlist)):
    image = Image.new("RGB", (1024, 1024), white)
    draw = ImageDraw.Draw(image)
    matrix = Hlist[i]
    
    mh.drawH(matrix, 1024, 0, 0, 2, draw)
    
    image.save('mask.PNG')
    os.startfile('mask.PNG')
    time.sleep(6)
    os.system("taskkill /im dllhost.exe")
    del image