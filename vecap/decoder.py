import skrf as rf
from skrf import micron
from skrf.media import Freespace
from skrf.calibration import OnePort
from copy import deepcopy
from unipath import Path
from matplotlib import pyplot as plt
from pylab import * # this is sloppy
from IPython.html.widgets import interactive

class Decoder(object):
    def __init__(self,base_dir, cal_template):
        '''
        A Decoder for a Vector Coded Aperture Measurment System
        
        Parameters 
        -----------
        base_dir : str, or `unipath.Path`
            the base directory which holds all data
            
        cal_template: `skrf.Calibration` object
            the calibration template that is copied for each mask's 
            calibration. The `measurements` attribute provided by 
            the calibraition template is never used, only the `ideals`
        '''
        self.cal_template = cal_template
        self.base_dir = Path( base_dir)
        # determine rank 
        max_dec = max([int(d) for d in self.decs.keys()])
        self.rank = int(sqrt(len('{0:b}'.format(max_dec))))
        
        self.frequency = rf.ran(str(self.decs.values()[0])).values()[0].frequency
    
    @property
    def decs(self):
        '''
        list of decimal values for each mask
        
        A dictionary with key:values as string:Path for each dec value
        '''
        return {str(k.name):k for k in self.base_dir.listdir()}
    
    
    def dec2mask(self,dec,**kw):
        '''
        translates a decimal representaion into a binary mask (numpy array) 
        '''
        rank =self.rank
        binary = binary_repr(int(dec), width=rank**2)
        return array([int(k) for k in binary ]).reshape((rank,rank),**kw)

    def mask2dec(self,mask):
        '''
        translates a mask to its decimal representation
        '''
        flat = mask.flatten().astype('str')
        return int('0b'+''.join(flat), base=0) 
    
    def pixel2decs(self,m,n, half_on_only=True):
        '''
        list of the masks which have a given pixel `on`.  

        the masks are given in decimal representations
        '''
        out=[]
        for d in self.decs.keys():
            mask = self.dec2mask(d)
            if mask[m,n] ==1:
                # pixel is on
                if half_on_only:
                    if sum(mask) == self.rank:
                        out.append(d)
                else:
                    out.append(d)
        return out
    
    def cal_of(self,dec):
        '''
        Calibration for a given mask, or pixel
        '''
        cal = deepcopy(self.cal_template)
        ideals = cal.ideals

        if isinstance(dec, tuple):
            # decode the measurements 
            measured =[]
            for ideal in ideals:
                m = self.raw_ntwk_of(dec,ideal.name)
                measured.append(m)
            
        else:
            measured = rf.ran(self.decs[dec]).values()
        

        cal.measured, cal.ideals = rf.align_measured_ideals(measured,ideals)
        cal.name = str(dec)
        return cal

    def error_ntwk_of(self,dec):
        '''
        error ntwk for a given mask, or pixel
        '''
        if isinstance(dec, tuple):
            ntwks = [self.error_ntwk_of(k) for k in self.pixel2decs(*dec)]
            return rf.average(ntwks)
        
        ntwk = self.cal_of(dec).error_ntwk
        ntwk.name = dec
        return ntwk
    
    def raw_ntwk_of(self,dec,name):
        '''
        raw ntwk for a given mask, or pixel
        '''
        if isinstance(dec, tuple):
            ntwks = [self.raw_ntwk_of(k,name) for k in self.pixel2decs(*dec)]
            return rf.average(ntwks)
        ntwk = rf.ran(str(self.decs[dec]), contains=name).values()[0]
        return ntwk
        
    def cor_ntwk_of(self,dec, name, loc='corrected'):
        '''
        corrected ntwk for a given mask, or pixel
        '''
        if isinstance(dec, tuple):
            if loc  == 'corrected':
                # decode in corrected-space
                ntwks = [self.cor_ntwk_of(k,name) for k in self.pixel2decs(*dec)]
                return rf.average(ntwks)
            elif loc =='measured':
                # decode in measured space
                m = self.raw_ntwk_of(dec,name)
                return self.cal_of(dec).apply_cal(m)
        
        # correct a measurement for a single mask
        return self.cal_of(dec).apply_cal(self.raw_ntwk_of(dec,name))
    
    
    
    def cor_cube(self,name,attr='s_db'):
        '''
        a corrected datacube
        
        constructs a `corrected`  3D data cube with dimensions 
        (FxMXN), where F is frequency axis, M and N are pixels 
        starting from upper left. 
        
        Parameters
        --------------
        name : str
            name of network
        attr: 's', 's_db', 's_deg', any skrf.Network property
            the attribute to put in the cube
        
        '''
        rank = self.rank
        z = array([getattr(self.cor_ntwk_of((m,n),name),attr) \
            for m in range(rank) for n in range(rank)])
        z = z.T.reshape(-1,rank,rank)
        return z
    
    def interact_cor_cube(self,name,attr='s_db', clims=None):
        '''
        an interactive image projection of the cor_cube
        '''
        z = self.cor_cube(name=name, attr=attr)
        if clims == None:
            if attr =='s_db':
                clims = (-20,10)
            elif attr=='s_deg':
                clims = (-180,180)
        freq = self.frequency    
        def func(n):
            plt.matshow(z[n])
            plt.title('%i%s'%(freq.f_scaled[n],freq.unit)) 
            plt.grid(0)
            plt.colorbar()
            if clims is not None:
                plt.clim(clims)
        return interactive (func,n =(0,len(freq)) )
