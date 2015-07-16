#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#04 June 2015

import skrf as rf
import os, os.path
from skrf import micron
import pylab
from matplotlib.pyplot import *

#this code may be taxing on your CPU if there ae a lot of data folders

dir1 = 'Cal'

folders = os.listdir(dir1)

os.chdir(dir1)

for x in range(0, len(folders)):
    
    DIR = folders[x]
    f = open("sParams.txt", "w")
    substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

    delta = 40*micron
    raw= rf.lat(DIR)

    freq = raw.values()[0].frequency
    air = rf.media.Freespace(frequency = freq, z0=50)

    ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)]
     #+[air.match(name = 'pl')] #add for pl files
    cal = rf.OnePort(measured = raw.values(), ideals = ideals, sloppy_input=True)

    f.write(str(cal.error_ntwk.s))
    f.close()

    figure()
    rf.NS(cal.caled_ntwks).plot_s_smith(marker ='.', ls='');
    title('Bingo Baby!')
    rf.legend_off()
    os.chdir(DIR)
    pylab.savefig('figure1.PNG')
    os.chdir('..')
    pylab.close()

    figure()
    title('Delay Shorts Magnitude')
    rf.NS(cal.caled_ntwks).plot_s_db();
    ylim(-1,1)
    os.chdir(DIR)
    pylab.savefig('figure2.PNG')
    os.chdir('..')
    pylab.close()

    figure()
    title('Calibration Standards Magnitude')
    rf.NS(cal.caled_ntwks[::-1]).plot_s_db();
    ylim(-60,10)
    os.chdir(DIR)
    pylab.savefig('figure3.PNG')
    os.chdir('..')
    pylab.close()

    figure()
    for ideal_ntwk, caled_ntwk in zip(cal.ideals, cal.caled_ntwks):
        if 'ds' in caled_ntwk.name:
            (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)

    ylim(-20,20);
    title('Delay Shorts De-trended Phase (Port 1)');
    os.chdir(DIR)
    pylab.savefig('figure4.PNG')
    os.chdir('..')
    pylab.close()

    #pylab.show()
os.chdir('..')

#throws an error at the end for any extra files at the end of the directory