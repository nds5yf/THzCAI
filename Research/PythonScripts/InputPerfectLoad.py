#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#08 June 2015

import os, os.path
import shutil

#make sure working directory is one level higher than all your data folders
#must first copy/paste the pl.s1p file into the same directory as your data folders
DIR = 'auto2x2'

folders = os.listdir(DIR)  #change

os.chdir(DIR)

for x in range(0, len(folders) - 1):
    shutil.copy('pl.s1p',folders[x])
    
os.chdir('..')