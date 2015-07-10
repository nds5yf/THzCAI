#Michael Eller
#Noah Sauber
#9 July 2015

import skrf as rf
import os
import devices as dev
from PIL import Image, ImageDraw
import subprocess
import math
import time as time

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

	def writeHText(self, o = '111-'):
		n = self.dimension
		f = open("matrices.txt", "w")
		f.write("These matrices are drawn in units of four recursively. Top left," + 
			"\n top right, bottom left, then bottom right. \n")
		for matrix in self.matrixList:
			f.write(matrix + '\n')
		f.close()

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

	def recursion_fix(self):
		li = self.matrixList    
		n = len(li) #Area and pixel count
		w = int(math.sqrt(n)) #Length and width, dimension
		b = self.dimension
		xloc = xcoor(b, [0], 0)
		yloc = ycoor(b, [0], 0)
		final = []
		for i in range (0, n):
			combo = li[i]
			temp = []
			temp2 = ""
			for j in range(0, n):
				temp.insert((xloc[j] + w*yloc[j]), combo[j])
			for j in range(0, len(temp)):    
				temp2 = temp2 + temp[j]
			final.append(temp2)
		return final    

	def pre_start(self):
		#move method will occasionally throw a timeout error
		#the first time it's called, so this will get that
		#out of the way before you start imaging
		esp = dev.ESP()
		esp.move(0)
		print esp.current_position()
		esp.move(1)
		print esp.current_position()

	def take_image(self):
		na = dev.ANA()
		esp = dev.ESP()
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

			esp.move(0)
			na.write_data('ds,0')
			esp.move(0.04)
			na.write_data('ds,1')
			esp.move(0.08)
			na.write_data('ds,2')
			esp.move(0.12)
			na.write_data('ds,3')
			esp.move(0.16)
			na.write_data('ds,4')
			esp.move(0.20)
			na.writeHText('ds,5')
			esp.move(0)

			os.chdir("..")
			os.system("taskkill /im dllhost.exe")
			time.sleep(1)

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