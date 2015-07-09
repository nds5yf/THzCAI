#Michael Eller
#Noah Sauber
#9 July 2015

import visa
from skrf.vi import vna
import numpy
import time as time

class ANA(object):
	def __init__(self):
		'''
		A class to easily take and write data with the vna

		@Params
			vna object from skrf.vi (zva)

		'''

		#you will want the ZVA to be connected when you initialize
		self.zva = vna.ZVA40(address=20)

	def write_data(self,name):

		self.zva.get_network().write_touchstone(name)

class ESP(object):
	def __init__(self):
		'''
		A class to control the ESP300 motor driver

		@Params
			visa instrument object
			current position
		'''
		rm = visa.ResourceManager()

		#assumes only one resource
		self.inst = rm.open_resource(rm.list_resources()[0])
		print(self.inst.query("*IDN?"))

	def current_position(self):
		
		return float(self.inst.ask('1TP'))

	def move(self, x):
		if self.current_position == x:
			return
		else:
			self.inst.write('1PA'+ numpy.str(x))
		while float(self.inst.ask('1TP')) - x != 0:
			time.sleep(0.01)

