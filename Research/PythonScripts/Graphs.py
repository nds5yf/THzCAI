#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#04 June 2015

import skrf as rf
from skrf import micron
import pylab
from matplotlib.pyplot import *

fileLocation = input("Input the path containing the data files (in quotations!): ")

dir = fileLocation
substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)

figure()
rf.NS(cal.caled_ntwks).plot_s_smith(marker ='.', ls='');
title('Bingo Baby!')
rf.legend_off()

figure()
title('Delay Shorts Magnitude')
rf.NS(cal.caled_ntwks).plot_s_db();
ylim(-1,1)

figure()
title('Calibration Standards Magnitude')
rf.NS(cal.caled_ntwks[::-1]).plot_s_db();
ylim(-60,10)

figure()
for ideal_ntwk, caled_ntwk in zip(cal.ideals, cal.caled_ntwks):
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');

pylab.show()