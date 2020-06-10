# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:44:41 2020

@author: Prabesh
"""

def qpsk_mod(bits,fc,fs):
    import numpy as np
    
# =============================================================================
#     splitting bits into even and odd bitstream
# =============================================================================
    I = bits[0::2]  # even bit stream
    Q = bits[1::2]  # odd bit stream
    
# =============================================================================
#     """using Upsample, FIR filter, and downsample for NRZ encoding"""
# =============================================================================
    OF = 8 # oversampling factor
    L = 2*OF # samples in each symbol
    
    from scipy.signal import upfirdn
    I = upfirdn(h = [1]*L, x=2*I-1, up=L) 
    Q = upfirdn(h = [1]*L, x=2*Q-1, up=L)
    
    t = np.arange(0,len(I)/fs,1/fs) # time
    
# =============================================================================
#     Quadrature carriers 
# =============================================================================
    
    I_t = I * np.cos(2*np.pi*fc*t)
    Q_t = -Q * np.sin(2*np.pi*fc*t)
    
    s = I_t + Q_t  #  QPSK modulated baseband signal
    
    #sst  = []
    #sst.append( I_t + Q_t)
    
    
    
    
    
    result = dict()  # a dictionary named result
    result['s(t)'] = s
  #   result['I(t)'] = I
 	# result['Q(t)'] = Q
  #   result['t'] = t
    #result['I_t(t)']=I_t
    #result['Q_t(t)']=Q_t
    

    
    return result






    












    
    
    
    




