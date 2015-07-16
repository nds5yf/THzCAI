#Michael Eller
#Noah Sauber
#9 July 2015

import skrf as rf
from skrf import micron
import os, os.path
import devices as dev
from PIL import Image, ImageDraw
import subprocess
import math
import time as time
import pylab
from matplotlib.pyplot import *

class Hadamard(object):
	def __init__(self, dimension, canvasSize):
		'''
		A class to hold all of the hadamard matrix methods

		@Params
		dimension: resolution of the mask
		resolution = 2^dimension 
		(dimension =1 -> 2x2, dimension = 2 -> 4x4)

		canvasSize: size of the mask image
		'''
		self.dimension = dimension
		self.canvasSize = canvasSize
		self.matrixList = createH(dimension,'111-', [])
		self.esp = dev.ESP()
		self.zva = dev.ZVA()

	def writeHText(self, o = '111-'):
		f = open("matrices_rec.txt", "w")
		for matrix in self.matrixList:
			f.write(matrix + '\n')
		f.close()
		f = open("matrices.txt", "w")
		temp = self.recursion_fix()
		for matrix in temp:
			f.write(matrix + '\n')
		f.close()

	def xcoor(self, n, li, x):
		if n == 0:
			return li
		else:
			dif = pow(2, x)
			temp = li[:]
			for i in range (0, len(li)):
				temp[i] = temp[i] + dif
			li = li + temp
			li = li + li
			return self.xcoor(n-1, li, x+1)

	def ycoor(self, n, li, x):
		if n == 0:
			return li
		else:
			dif = pow(2, x)
			li = li + li
			temp = li[:]
			for i in range (0, len(li)):
				temp[i] = temp[i] + dif
			li = li + temp
			return self.ycoor(n-1, li, x+1)

	def recursion_fix(self):
		li = self.matrixList
		n = len(li) #Area and pixel count
		w = int(math.sqrt(n)) #Length and width
		b = self.dimension #Times of iteration
		xloc = self.xcoor(b, [0], 0)
		yloc = self.ycoor(b, [0], 0)
		final = []
		for i in range (0, n):
			combo = li[i]
			temp = [0]*n
			temp2 = ""
			for j in range(0, n):
				tot = xloc[j] + w*yloc[j]
				temp[tot] = combo[j]
			for j in range(0, len(temp)):    
				temp2 = temp2 + temp[j]
			final.append(temp2)
		return final     

	def pre_start(self):
		#move method will occasionally throw a timeout error
		#the first time it's called, so this will get that
		#out of the way before you start imaging
		self.esp.move(0)
		self.esp.move(1)
		self.esp.move(0)

	def take_image(self):
		white = (255, 255, 255)
		hlist = self.matrixList
		size = self.canvasSize
		for i in range(0, len(hlist)):
			image = Image.new("RGB", (size, size), white)
			draw = ImageDraw.Draw(image)
			matrix = hlist[i]

			#start drawing!
			drawH(matrix, size, 0, 0, 2, draw)

			#start collecting data!
			image.save("mask.png")
			time.sleep(0.5)
			del image
			os.startfile('mask.png')
			time.sleep(2)

			#create files and save data!
			os.makedirs(str(i))
			os.chdir(str(i))

			self.zva.write_data('ds,0')
			self.esp.move(0.04)
			self.zva.write_data('ds,1')
			self.esp.move(0.08)
			self.zva.write_data('ds,2')
			self.esp.move(0.12)
			self.zva.write_data('ds,3')
			self.esp.move(0.16)
			self.zva.write_data('ds,4')
			self.esp.move(0.20)
			self.zva.write_data('ds,5')
			self.esp.move(0)

			os.chdir("..")
			os.system("taskkill /im dllhost.exe")
			time.sleep(1)

	def noah_image(self):
		self.esp.move(0)
		white = (255, 255, 255)
		hlist = self.recursion_fix()
		size = self.canvasSize
		for i in range(0, len(hlist)):
			image = Image.new("RGB", (size, size), white)
			draw = ImageDraw.Draw(image)
			matrix = hlist[i]
			
			paintH(matrix, size, draw)

			#start collecting data!
			image.save("mask.png")
			time.sleep(0.5)
			del image
			os.startfile('mask.png')
			time.sleep(2)
			
			#create files and save data!
			filename = str(int((format2bn(matrix)), 2))
			os.makedirs(filename)
			os.chdir(filename)
			
			self.esp.move(0)
			self.zva.write_data('ds,0')
			self.esp.move(0.04)
			self.zva.write_data('ds,1')
			self.esp.move(0.08)
			self.zva.write_data('ds,2')
			self.esp.move(0.12)
			self.zva.write_data('ds,3')
			self.esp.move(0.16)
			self.zva.write_data('ds,4')
			self.esp.move(0.20)
			self.zva.write_data('ds,5')
			self.esp.move(0)
			
			os.chdir("..")
			os.system("taskkill /im dllhost.exe")
			time.sleep(1)

	def calibrate(self):
		DIR = 'cal'
		os.makedirs(DIR)
		os.chdir(DIR)
		self.esp.move(0)
		self.zva.write_data('ds,0')
		self.esp.move(0.04)
		self.zva.write_data('ds,1')
		self.esp.move(0.08)
		self.zva.write_data('ds,2')
		self.esp.move(0.12)
		self.zva.write_data('ds,3')
		self.esp.move(0.16)
		self.zva.write_data('ds,4')
		self.esp.move(0.20)
		self.zva.write_data('ds,5')
		self.esp.move(0)
		#save the smith plot and s params!
		os.chdir('..')
		#does not work with new version of skrf
		'''
		#f = open("sParams.txt", "w")
		substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane
		delta = 40*micron
		raw = rf.lat(DIR)
		freq = raw.values()[0].frequency
		air = rf.media.Freespace(frequency = freq, z0=50)
		ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)]
		#+[air.match(name = 'pl')] #add for pl files
		cal = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)
		#f.write(str(cal.error_ntwk.s))
		#f.close()
		figure()
		rf.NS(cal.caled_ntwks).plot_s_smith(marker ='.', ls='')
		title('Bingo Baby!')
		rf.legend_off()
		os.chdir(DIR)
		pylab.savefig('figure1.PNG')
		pylab.close()
		os.chdir('..')
		'''

	def rename_folders(self, base_dir):
		matrixList = self.recursion_fix()
		os.chdir(base_dir)
		for x in range(0, len(matrixList)):
			os.rename(str(x), str(int(format2bn(matrixList[x]), 2)))

#simply turn -'s to 1's and vice versa
def inverse(s):
	string = ""
	for x in range(0, len(s)):
		if s[x] == '-':
			string += '1'
		else:
			string += '-'
	return string

#turn 1's to 0's and -'s to 1's
def format2bn(s):
	string = ""
	for x in range(0, len(s)):
		if s[x] == '-':
			string += '1'
		else:
			string += '0'
	return string

#rotating the h matrix to create the different combos 
#'s' is the string to shift, 'n' is how many times
def shift(s, n):
	temp = s
	for i in range(0, n):
		x = len(temp)/4
		l = len(temp)
		string = temp[l - x:] +temp[:l - x]
		temp = string
	return string

#create Hadamard matrices recursively
#'o' should be '111-' or some permutation on the initial call
#'n' is depth of recursion 0 = nothing 1 = 2x2 2 = 4x4 etc...
def createH(n, o, rlist):
	if n == 0:
		return rlist
	rlist.append(o)
	s = ""
	s += o
	s += o
	s += o
	s += inverse(o)
	rlist = createH(n - 1, s, rlist)
	o = shift(o, 1)
	rlist.append(o)
	s = ""
	s += o
	s += o
	s += o
	s += inverse(o)
	rlist = createH(n - 1, s, rlist)
	o = shift(o, 2)
	rlist.append(o)
	s = ""
	s += o
	s += o
	s += o
	s += inverse(o)
	rlist = createH(n - 1, s, rlist)
	o = shift(o, 3)
	rlist.append(o)
	s = ""
	s += o
	s += o
	s += o
	s += inverse(o)
	rlist = createH(n - 1, s, rlist)
	rlist.sort(key = len)
	#delete all combos that are not NxN (the smaller ones)
	counter = 0
	for x in range(0, len(rlist)):
		l = len(rlist[len(rlist) - 1])
		if len(rlist[x]) < l:
			counter += 1
	del rlist[0 : counter]
	return rlist

#draw the Hadamard Matrix recursively
#'matrix' is the string to be converted to an image
#'canvasSize' remains constant, 'x' and 'y' must be 0 to start
#'im' is the image draw object
#'n' must be 2 to start
def drawH(matrix, canvasSize, x, y, n, im):
	if len(matrix) == 4:
		for i in range(0,4):
			if matrix[i] == '1':
				im.rectangle(((x, y), (x + canvasSize / n, y + canvasSize / n)),
					fill = 'black', outline = 'black')
			if i == 1:
				x -= canvasSize / n
				y += canvasSize / n
			else:
				x += canvasSize / n
	else:
		s1 = matrix[0:len(matrix)/4]
		s2 = matrix[len(matrix) / 4 : len(matrix) / 2]
		s3 = matrix[len(matrix) / 2 : 3 * len(matrix) / 4]
		s4 = matrix[3 * len(matrix) / 4 : len(matrix)]
		drawH(s1, canvasSize, x, y, 2 * n, im)
		drawH(s2, canvasSize, x + canvasSize / n, y, 2 * n, im)
		drawH(s3, canvasSize, x, y + canvasSize / n, 2 * n, im)
		drawH(s4, canvasSize, x + canvasSize / n, y + canvasSize / n, 2 * n, im)

def paintH(matrix, canvasSize, draw):
	counter = 0
	x = len(matrix)
	z = int(math.sqrt(x))
	xloc = 0
	yloc = 0
	for i in range(0, x):
		counter += 1
		if matrix[i] == '1':
			draw.rectangle(((xloc, yloc), (xloc + canvasSize/z, yloc + canvasSize/z)), fill='black', outline='black')
		xloc += canvasSize/z
		if counter == z:
			counter = 0
			xloc = 0
			yloc += canvasSize/z        
  
