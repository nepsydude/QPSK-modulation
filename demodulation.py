# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:58:24 2020

@author: Prabesh
"""

import numpy as np
def qpsk_demodule(r,fc,OF):
    fc = 100 # carrier frequency in Hz
    OF = 8 # over sampling factor
    fs = OF*fc #sampling frequency
    L = 2*OF #samples in each symbol
    
    t = np.arange(0,len(r)/fs,1/fs) # time
    
    x=r*np.cos(2*np.pi*fc*t) # I arm
    y=-r*np.sin(2*np.pi*fc*t) # Q arm
    """discrete, linear convolution of two one-dimensional sequences
        with numpy.convolve"""
    x = np.convolve(x,np.ones(L)) # integrate for L (Tsym=2*Tb) duration
    y = np.convolve(y,np.ones(L)) #integrate for L (Tsym=2*Tb) duration
    
    x = x[L-1::L] # I arm - sample at every symbol instant Tsym
    y = y[L-1::L] # Q arm - sample at every symbol instant Tsym
    
    bits_det = np.zeros(2*len(x)) # output bits after detection
    bits_det[0::2] = (x>0) # even bits
    bits_det[1::2] = (y>0) # odd bits
    
    return bits_det
    

    
    
    
    
    
    
    
    