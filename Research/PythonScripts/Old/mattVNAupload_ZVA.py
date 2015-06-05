# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:24:27 2012

@author: measurement
"""

from skrf import mathFunctions as mf

errorNetwork = cal1.error_ntwk ## cal1 only applies to ** FIRST ** CALIBRATION
                               ## FROM CAI_v1.py

directivity = errorNetwork.s[:,0,0]
sourceMatch = errorNetwork.s[:,1,1]
refTrack = errorNetwork.s[:,0,1]*errorNetwork.s[:,1,0]

directivityString = ''.join(['%s, '%k for k in mf.complex2Scalar(directivity)])
sourceMatchString = ''.join(['%s, '%k for k in mf.complex2Scalar(sourceMatch)])
refTrackString = ''.join(['%s, '%k for k in mf.complex2Scalar(refTrack)])
#trim trailing whitespace/comma...
directivityString = directivityString[0:-2]
sourceMatchString = sourceMatchString[0:-2]
refTrackString = refTrackString[0:-2]

my_vna.write("CORR:COLL:METH:DEF 'mattTmpCal',FOPort,3")
my_vna.write("CORR:COLL:SAVE:SEL:DEF")
my_vna.write("INIT:CONT OFF; :INIT; *WAI")
my_vna.write("CORR:CDAT 'REFLTRACK',3,0," + refTrackString)
my_vna.write("CORR:CDAT 'SRCMATCH',3,0," + sourceMatchString)
my_vna.write("CORR:CDAT 'DIRECTIVITY',3,0," + directivityString)
my_vna.write("INIT:CONT ON")