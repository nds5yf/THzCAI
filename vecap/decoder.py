import skrf as rf
from skrf import micron
from skrf.media import Freespace
from skrf.calibration import OnePort
from copy import deepcopy
from unipath import Path
from matplotlib import pyplot as plt
from pylab import * # this is sloppy
from IPython.html.widgets import interactive



# conversion between masks representations: mask  and decimal 
# ( binary is an intermediary form).
def dec2bin( dec, rank):
    '''
    convert decimal to binary with given width
    '''
    binary = binary_repr(int(dec), width=rank**2)
    return binary
    
def dec2mask(dec,rank,**kw):
    '''
    translates a decimal representaion into a binary mask (numpy array) 
    '''
    binary = dec2bin(dec=dec,rank=rank)
    return array([int(k) for k in binary ]).reshape((rank,rank),**kw)
    
def bin2dec(binary):
    '''
    convert binary to decimal
    '''
    return int('0b'+''.join(binary), base=0) 
    
def mask2dec(mask):
    '''
    translates a mask to its decimal representation
    '''
    flat = mask.flatten().astype('str')
    return bin2dec(flat)

# creation of mask sets for a given rank
def gen_had_masks(rank, invert=False):
    '''
    generate a list  hadamard masks for a given rank 
    
    
    the masks returned are binary numpy.arrays's.
    there will be N=rank**2 masks. 
    '''
    raise NotImplementedError()
    
def gen_raster_masks(rank, invert=False):
    '''
    generate a list  raster masks for a given rank 
    
    the masks returned are binary numpy.arrays's.
    there will be N=rank**2 masks. 
    '''
    raise NotImplementedError()

def gen_masks(kind, rank, invert=False):
    '''
    generate set of masks of given `kind` and rank. possibly inverted
    '''
    kw =dict(rank=rank, invert=invert)
    if kind ==hadamard:
        return had_masks_from_rank(**kw)
    elif kind == 'raster':
        return raster_masks_from_rank(**kw)
    else:
        raise ValueError('bad kind')
    

def dec_from_rank(kind, rank, invert=False):
    '''
    create a decimal representations for a given kind of mask set and rank
    
    '''
    masks= had_masks_from_rank(kind=kind, rank=rank, invert=invert)
    return [mask2dec(k) for k in masks]



class Decoder(object):
    def __init__(self,base_dir, cal=None, cal_each_mask=False):
        '''
        A Decoder for a Vector Coded Aperture Measurment System
        
        Parameters 
        -----------
        base_dir : str, or `unipath.Path`
            the base directory which holds all data
            
        cal: `skrf.Calibration` object or None
            the calibration template that is copied for each mask's 
            calibration. The `measurements` attribute provided by 
            the calibraition template is never used, only the `ideals`.
            if None, then no calibration is performed
        
        cal_each_mask : bool
            should a calibration be performed for each mask? If True, this 
            requires that `cal` represents a calibration template, for 
            which the `measurements` are provided for each mask dir 
        '''
        self.base_dir = Path( base_dir)
        self.cal = cal
                
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
    
    
    
            
    def pixel2decs(self,m,n, half_on_only=True):
        '''
        list of the masks which have a given pixel `on`.  

        the masks are given in decimal representations
        '''
        out=[]
        for d in self.decs.keys():
            mask = dec2mask(d, rank=self.rank)
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
        
        ##TODO: for no-cal or static cal this could be only calculated
        # once to improve performance
        if self.cal is None:
            freq = self.frequency
            n = len(freq)
            coefs ={'directivity':zeros(n),
                    'source match': zeros(n),
                    'reflection tracking':ones(n)}
            cal =OnePort.from_coefs(frequency=freq, coefs=coefs)
            return cal
            
        if not cal_each_mask:
            return self.cal
        else:
            # we want a calibration for each mask, so create the calbration
            # for this mask,or pixel
            cal = deepcopy(self.cal)
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


