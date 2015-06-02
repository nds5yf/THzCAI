## cal1,cal2,cal3,cal4 are 4 calibrations for 4 masks
## error networks should be saved
## to proceed when prompted, type anything in and hit "enter"
## Steps: Take 4 mask calibrations (w/ 5 regular standards) ---> Take data from each Mask

import skrf as rf # from intro.py
import pyvisa 
from skrf.vi import vna
import os
from os.path import join  # from chunk1.py
from skrf import micron
import pylab
import matplotlib.pyplot
my_vna=vna.ZVA40(address=20)

#----------------------------------- SET 1 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 1?: ")
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='Test'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal1 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal1.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal1 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal1.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal1 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal1.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal1 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal1.ideals, cal1.caled_ntwks):
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      ## change!!
cal1.error_ntwk.write_touchstone('errorNetworkCal1')   ## change!!
savefig('Cal1 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 2 Cal?: ")
print str

#----------------------------------- SET 2 Cal --------------------------------#
os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal2')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 2?: ")
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='Cal2'
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal2 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)

rf.NS(cal2.caled_ntwks).plot_s_smith(marker ='.', ls='');
title('Bingo Baby!')
rf.legend_off()
savefig('Cal2 Figure 1.png')

figure()
title('Delay Shorts Magnitude')
rf.NS(cal2.caled_ntwks).plot_s_db();
ylim(-1,1)
savefig('Cal2 Figure 2.png')

figure()
title('Calibration Standards Magnitude')
rf.NS(cal2.caled_ntwks[::-1]).plot_s_db();
ylim(-60,10)
savefig('Cal2 Figure 3.png')

figure()
for ideal_ntwk, caled_ntwk in zip(cal2.ideals, cal2.caled_ntwks):
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');
cal2.error_ntwk.write_touchstone('errorNetworkCal2')
savefig('Cal2 Figure 4.png')

str = raw_input("Ready to move to Set 3 Cal?: ")
print str

#----------------------------------- SET 3 Cal --------------------------------#
os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal3')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 3?: ")
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='Cal3'
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal3 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)

rf.NS(cal3.caled_ntwks).plot_s_smith(marker ='.', ls='');
title('Bingo Baby!')
rf.legend_off()
savefig('Cal3 Figure 1.png')

figure()
title('Delay Shorts Magnitude')
rf.NS(cal3.caled_ntwks).plot_s_db();
ylim(-1,1)
savefig('Cal3 Figure 2.png')

figure()
title('Calibration Standards Magnitude')
rf.NS(cal3.caled_ntwks[::-1]).plot_s_db();
ylim(-60,10)
savefig('Cal3 Figure 3.png')

figure()
for ideal_ntwk, caled_ntwk in zip(cal3.ideals, cal3.caled_ntwks):
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');
cal3.error_ntwk.write_touchstone('errorNetworkCal3')
savefig('Cal3 Figure 4.png')

str = raw_input("Ready to move to Set 4 Cal?: ")
print str

#----------------------------------- SET 4 Cal --------------------------------#
os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal4')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 4?: ")
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='Cal4'
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal4 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)

rf.NS(cal4.caled_ntwks).plot_s_smith(marker ='.', ls='');
title('Bingo Baby!')
rf.legend_off()
savefig('Cal4 Figure 1.png')

figure()
title('Delay Shorts Magnitude')
rf.NS(cal4.caled_ntwks).plot_s_db();
ylim(-1,1)
savefig('Cal4 Figure 2.png')

figure()
title('Calibration Standards Magnitude')
rf.NS(cal4.caled_ntwks[::-1]).plot_s_db();
ylim(-60,10)
savefig('Cal4 Figure 3.png')

figure()
for ideal_ntwk, caled_ntwk in zip(cal4.ideals, cal4.caled_ntwks):
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');
cal4.error_ntwk.write_touchstone('errorNetworkCal4')
savefig('Cal4 Figure 4.png')


str = raw_input("Ready to move to Set 5 Cal?: ")
print str

#----------------------------------- SET 5 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 5?: ")
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal5 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal5.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal5 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal5.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal5 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal5.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal5 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal5.ideals, cal5.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal5.error_ntwk.write_touchstone('errorNetworkCal5')   ## change!!   ## change!!
savefig('Cal5 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 6 Cal?: ")      ## change!!
print str

#----------------------------------- SET 6 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 6?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal6 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal6.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal6 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal6.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal6 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal6.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal6 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal6.ideals, cal6.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal6.error_ntwk.write_touchstone('errorNetworkCal6')   ## change!!  ## change!!
savefig('Cal6 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 7 Cal?: ")      ## change!!
print str

#----------------------------------- SET 7 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 7?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal7 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal7.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal7 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal7.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal7 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal7.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal7 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal7.ideals, cal7.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal7.error_ntwk.write_touchstone('errorNetworkCal7')   ## change!!  ## change!!
savefig('Cal7 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 8 Cal?: ")      ## change!!
print str

#----------------------------------- SET 8 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 8?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal8 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal8.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal8 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal8.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal8 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal8.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal8 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal8.ideals, cal8.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal8.error_ntwk.write_touchstone('errorNetworkCal8')   ## change!!  ## change!!
savefig('Cal8 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 9 Cal?: ")      ## change!!
print str

#----------------------------------- SET 9 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 9?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal9 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)  ## change!!

rf.NS(cal9.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal9 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal9.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal9 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal9.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal9 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal9.ideals, cal9.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal9.error_ntwk.write_touchstone('errorNetworkCal9')   ## change!!  ## change!!
savefig('Cal9 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 10 Cal?: ")      ## change!!
print str

#----------------------------------- SET 10 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 10?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal10 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal10.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal10 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal10.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal10 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal10.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal10 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal10.ideals, cal10.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal10.error_ntwk.write_touchstone('errorNetworkCal10')   ## change!!  ## change!!
savefig('Cal10 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 11 Cal?: ")      ## change!!
print str

#----------------------------------- SET 11 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 11?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal11 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal11.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal11 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal11.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal11 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal11.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal11 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal11.ideals, cal11.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal11.error_ntwk.write_touchstone('errorNetworkCal11')   ## change!!  ## change!!
savefig('Cal11 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 12 Cal?: ")      ## change!!
print str

#----------------------------------- SET 12 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 12?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal12 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal12.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal12 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal12.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal12 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal12.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal12 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal12.ideals, cal12.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal12.error_ntwk.write_touchstone('errorNetworkCal12')   ## change!!  ## change!!
savefig('Cal12 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 13 Cal?: ")      ## change!!
print str

#----------------------------------- SET 13 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 13?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal13 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal13.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal13 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal13.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal13 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal13.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal13 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal13.ideals, cal13.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal13.error_ntwk.write_touchstone('errorNetworkCal13')   ## change!!  ## change!!
savefig('Cal13 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 14 Cal?: ")      ## change!!
print str

#----------------------------------- SET 14 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 14?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal14 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal14.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal14 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal14.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal14 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal14.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal14 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal14.ideals, cal14.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal14.error_ntwk.write_touchstone('errorNetworkCal14')   ## change!!  ## change!!
savefig('Cal14 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 15 Cal?: ")      ## change!!
print str

#----------------------------------- SET 15 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 15?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal15 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal15.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal15 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal15.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal15 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal15.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal15 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal15.ideals, cal15.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal15.error_ntwk.write_touchstone('errorNetworkCal15')   ## change!!  ## change!!
savefig('Cal15 Figure 4.png')                          ## change!!

str = raw_input("Ready to move to Set 16 Cal?: ")      ## change!!
print str

#----------------------------------- SET 16 Cal --------------------------------#
#os.chdir('C:\Users\Henry Bishop\Documents\Research\Cal1')  # ensure it gets to correct folder location for this set
str = raw_input("Ready to calibrate set 16?: ")  ## change!!
print str
my_vna.s11.write_touchstone('ds,0')
str = raw_input("Ready to take ds,1?: ")
print str
my_vna.s11.write_touchstone('ds,1')
str = raw_input("Ready to take ds,2?: ")
print str
my_vna.s11.write_touchstone('ds,2')
str = raw_input("Ready to take ds,3?: ")
print str
my_vna.s11.write_touchstone('ds,3')
str = raw_input("Ready to take ds,4?: ")
print str
my_vna.s11.write_touchstone('ds,4')
str = raw_input("Ready to take ds,5?: ")
print str
my_vna.s11.write_touchstone('ds,5')
str = raw_input("Ready to take pl?: ")
print str
my_vna.s11.write_touchstone('pl')
str = raw_input("Ready to see results?: ")
print str
# from chunk1.py
## input 
os.chdir('..')
dir ='CAI 3.2'   ## change!!
write_caled_duts= True

substrate_thickness = 430e-6 # needed to re-embed measurements to reference plane

###


delta = 40*micron
raw= rf.lat(dir)

freq = raw.values()[0].frequency
air = rf.media.Freespace(frequency = freq, z0=50)

ideals = [ air.delay_short(k*delta, name='ds,%i'%k) for k in range(6)] +\
         [air.match(name = 'pl')]
cal16 = rf.Calibration(measured = raw.values(), ideals = ideals, sloppy_input=True)## change!!

rf.NS(cal16.caled_ntwks).plot_s_smith(marker ='.', ls='');   ## change!!
title('Bingo Baby!')
rf.legend_off()
savefig('Cal16 Figure 1.png')           ## change!!

figure()
title('Delay Shorts Magnitude')
rf.NS(cal16.caled_ntwks).plot_s_db();    ## change!!
ylim(-1,1)  
savefig('Cal16 Figure 2.png')            ## change!!

figure()
title('Calibration Standards Magnitude')
rf.NS(cal16.caled_ntwks[::-1]).plot_s_db();   ## change!!
ylim(-60,10)
savefig('Cal16 Figure 3.png')            ## change!!

figure()
for ideal_ntwk, caled_ntwk in zip(cal16.ideals, cal16.caled_ntwks):  ## change!!  ## change!!
    if 'ds' in caled_ntwk.name:
        (caled_ntwk/ideal_ntwk).plot_s_deg(0,0)        

ylim(-20,20);
title('Delay Shorts De-trended Phase (Port 1)');      
cal16.error_ntwk.write_touchstone('errorNetworkCal16')   ## change!!  ## change!!
savefig('Cal16 Figure 4.png')                          ## change!!

#----------------------------------- Data --------------------------------#

## USE FOR REGULAR DATA COLLECTION
my_vna.s11.write_touchstone('Silicon')
device = rf.N('Silicon.s1p')
device.plot_s_db()
savefig('Data_dB.png')
device.plot_s_deg()
savefig('Data_Deg.png')
##

str = raw_input("Ready to take data from Mask 1?: ")
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal1')  # ensure it gets to correct folder location for this set
my_vna.s11.write_touchstone('Mask1Data')
device=rf.N('Mask1Data.s1p')
caled1=cal1.apply_cal(device)
caled1.write_touchstone(filename='CaledMask1Data')
caled1.plot_s_db()
savefig('Cal1dB.png')
caled1.plot_s_deg()
savefig('Cal1Deg.png')

str = raw_input("Ready to take data from Mask 2?: ")
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal2')  # ensure it gets to correct folder location for this set
my_vna.s11.write_touchstone('Mask2Data')
device2=rf.N('Mask2Data.s1p')
caled2=cal2.apply_cal(device2)
caled2.write_touchstone(filename='CaledMask2Data')
caled2.plot_s_db()
savefig('Cal2dB.png')
caled2.plot_s_deg()
savefig('Cal2Deg.png')

str = raw_input("Ready to take data from Mask 3?: ")
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal3')  # ensure it gets to correct folder location for this set
my_vna.s11.write_touchstone('Mask3Data')
device3=rf.N('Mask3Data.s1p')
caled3=cal3.apply_cal(device3)
caled3.write_touchstone(filename='CaledMask3Data')
caled3.plot_s_db()
savefig('Cal3dB.png')
caled3.plot_s_deg()
savefig('Cal3Deg.png')

str = raw_input("Ready to take data from Mask 4?: ")
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal4')  # ensure it gets to correct folder location for this set
my_vna.s11.write_touchstone('Mask4Data')
device4=rf.N('Mask4Data.s1p')
caled4=cal4.apply_cal(device4)
caled4.write_touchstone(filename='CaledMask4Data')
caled4.plot_s_db()
savefig('Cal4dB.png')
caled4.plot_s_deg()
savefig('Cal4Deg.png')

str = raw_input("Ready to take data from Mask 5?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal5')  ## change!!
my_vna.s11.write_touchstone('Mask5Data')  ## change!!
device5=rf.N('Mask5Data.s1p') ## change!! ## change!!
caled5=cal5.apply_cal(device5) ## change!! ## change!! ## change!!
caled5.write_touchstone(filename='CaledMask5Data') ## change!!  ## change!!
caled5.plot_s_db()  ## change!!
savefig('Cal5dB.png')  ## change!!
caled5.plot_s_deg()   ## change!!
savefig('Cal5Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 6?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal6')  ## change!!
my_vna.s11.write_touchstone('Mask6Data')  ## change!!
device6=rf.N('Mask6Data.s1p') ## change!! ## change!!
caled6=cal6.apply_cal(device6) ## change!! ## change!! ## change!!
caled6.write_touchstone(filename='CaledMask6Data') ## change!!  ## change!!
caled6.plot_s_db()  ## change!!
savefig('Cal6dB.png')  ## change!!
caled6.plot_s_deg()   ## change!!
savefig('Cal6Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 7?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal7')  ## change!!
my_vna.s11.write_touchstone('Mask7Data')  ## change!!
device7=rf.N('Mask7Data.s1p') ## change!! ## change!!
caled7=cal7.apply_cal(device7) ## change!! ## change!! ## change!!
caled7.write_touchstone(filename='CaledMask7Data') ## change!!  ## change!!
caled7.plot_s_db()  ## change!!
savefig('Cal7dB.png')  ## change!!
caled7.plot_s_deg()   ## change!!
savefig('Cal7Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 8?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal8')  ## change!!
my_vna.s11.write_touchstone('Mask8Data')  ## change!!
device8=rf.N('Mask8Data.s1p') ## change!! ## change!!
caled8=cal8.apply_cal(device8) ## change!! ## change!! ## change!!
caled8.write_touchstone(filename='CaledMask8Data') ## change!!  ## change!!
caled8.plot_s_db()  ## change!!
savefig('Cal8dB.png')  ## change!!
caled8.plot_s_deg()   ## change!!
savefig('Cal8Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 9?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal9')  ## change!!
my_vna.s11.write_touchstone('Mask9Data')  ## change!!
device9=rf.N('Mask9Data.s1p') ## change!! ## change!!
caled9=cal9.apply_cal(device9) ## change!! ## change!! ## change!!
caled9.write_touchstone(filename='CaledMask9Data') ## change!!  ## change!!
caled9.plot_s_db()  ## change!!
savefig('Cal9dB.png')  ## change!!
caled9.plot_s_deg()   ## change!!
savefig('Cal9Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 10?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal10')  ## change!!
my_vna.s11.write_touchstone('Mask10Data')  ## change!!
device10=rf.N('Mask10Data.s1p') ## change!! ## change!!
caled10=cal10.apply_cal(device10) ## change!! ## change!! ## change!!
caled10.write_touchstone(filename='CaledMask10Data') ## change!!  ## change!!
caled10.plot_s_db()  ## change!!
savefig('Cal10dB.png')  ## change!!
caled10.plot_s_deg()   ## change!!
savefig('Cal10Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 11?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal11')  ## change!!
my_vna.s11.write_touchstone('Mask11Data')  ## change!!
device11=rf.N('Mask11Data.s1p') ## change!! ## change!!
caled11=cal11.apply_cal(device11) ## change!! ## change!! ## change!!
caled11.write_touchstone(filename='CaledMask11Data') ## change!!  ## change!!
caled11.plot_s_db()  ## change!!
savefig('Cal11dB.png')  ## change!!
caled11.plot_s_deg()   ## change!!
savefig('Cal11Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 12?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal12')  ## change!!
my_vna.s11.write_touchstone('Mask12Data')  ## change!!
device12=rf.N('Mask12Data.s1p') ## change!! ## change!!
caled12=cal12.apply_cal(device12) ## change!! ## change!! ## change!!
caled12.write_touchstone(filename='CaledMask12Data') ## change!!  ## change!!
caled12.plot_s_db()  ## change!!
savefig('Cal12dB.png')  ## change!!
caled12.plot_s_deg()   ## change!!
savefig('Cal12Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 13?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal13')  ## change!!
my_vna.s11.write_touchstone('Mask13Data')  ## change!!
device13=rf.N('Mask13Data.s1p') ## change!! ## change!!
caled13=cal13.apply_cal(device13) ## change!! ## change!! ## change!!
caled13.write_touchstone(filename='CaledMask13Data') ## change!!  ## change!!
caled13.plot_s_db()  ## change!!
savefig('Cal13dB.png')  ## change!!
caled13.plot_s_deg()   ## change!!
savefig('Cal13Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 14?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal14')  ## change!!
my_vna.s11.write_touchstone('Mask14Data')  ## change!!
device14=rf.N('Mask14Data.s1p') ## change!! ## change!!
caled14=cal14.apply_cal(device14) ## change!! ## change!! ## change!!
caled14.write_touchstone(filename='CaledMask14Data') ## change!!  ## change!!
caled14.plot_s_db()  ## change!!
savefig('Cal14dB.png')  ## change!!
caled14.plot_s_deg()   ## change!!
savefig('Cal14Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 15?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal15')  ## change!!
my_vna.s11.write_touchstone('Mask15Data')  ## change!!
device15=rf.N('Mask15Data.s1p') ## change!! ## change!!
caled15=cal15.apply_cal(device15) ## change!! ## change!! ## change!!
caled15.write_touchstone(filename='CaledMask15Data') ## change!!  ## change!!
caled15.plot_s_db()  ## change!!
savefig('Cal15dB.png')  ## change!!
caled15.plot_s_deg()   ## change!!
savefig('Cal15Deg.png')  ## change!!

str = raw_input("Ready to take data from Mask 16?: ")  ## change!!
print str
os.chdir('C:\Users\Henry Bishop\Documents\Research\CAI 3.2\Cal16')  ## change!!
my_vna.s11.write_touchstone('Mask16Data')  ## change!!
device16=rf.N('Mask16Data.s1p') ## change!! ## change!!
caled16=cal16.apply_cal(device16) ## change!! ## change!! ## change!!
caled16.write_touchstone(filename='CaledMask16Data') ## change!!  ## change!!
caled16.plot_s_db()  ## change!!
savefig('Cal16dB.png')  ## change!!
caled16.plot_s_deg()   ## change!!
savefig('Cal16Deg.png')  ## change!!


#----------------------------------- Backing out Image --------------------------------#

M = np.array(([1,1,1,1,],[1,0,1,0],[1,1,0,0],[1,0,0,1]))  #Mask array
b1 = rf.io.touchstone.Touchstone('CaledMask1Data.s1p').get_sparameter_data('ri')
b2 = rf.io.touchstone.Touchstone('CaledMask2Data.s1p').get_sparameter_data('ri')
b3 = rf.io.touchstone.Touchstone('CaledMask3Data.s1p').get_sparameter_data('ri')
b4 = rf.io.touchstone.Touchstone('CaledMask4Data.s1p').get_sparameter_data('ri')

B1 = []
temp = []
for key, value in b1.iteritems():
    temp = [key,value]
    B1.append(temp)
B1 = np.array(B1[0][1])
    
B2 = []
for key, value in b2.iteritems():
    temp = [key,value]
    B2.append(temp)
B2 = np.array(B2[0][1])

B3 = []
for key, value in b3.iteritems():
    temp = [key,value]
    B3.append(temp)
B3 = np.array(B3[0][1])    

B4 = []
for key, value in b4.iteritems():
    temp = [key,value]
    B4.append(temp)
B4 = np.array(B4[0][1])    
    
bTotal = np.array([B1,B2,B3,B4])
x = np.linalg.solve(M,bTotal)
x