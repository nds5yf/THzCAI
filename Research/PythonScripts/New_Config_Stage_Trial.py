#Stage setup
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#25 June 2015

from stages import *

esp= ESP300()
esp.current_axis=1
esp.units= 'millimeter'

#esp.position = 0

#need to modify code to move in the positive direction