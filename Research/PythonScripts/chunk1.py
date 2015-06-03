from os.path import join 
import skrf as rf
from skrf import micron
import pylab
import matplotlib.pyplot

## input 
dir ='temp1' 
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###
## my_vna.s11.write_touchstone('pl')



delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)

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