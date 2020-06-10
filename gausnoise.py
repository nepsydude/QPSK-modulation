# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:07:23 2020

@author: Prabesh
"""


def AWGN(s,N):
    
    import numpy as np
    import math
    #from modulation import qpsk_mod
    
    
    # w = np.sqrt(N*np.var(s)*10**(EbN0dB/10.)/2.)*(np.random.randn(len(s)) + 1j*np.random.randn(len(s)))  
    # r = s + w                          
    snrdB = 30
    snrlin = 10**(snrdB/10) # SNR to linear scale
    # N = 10000 # Number of symbols to transmit
    #bits = np.random.randint(2, size=N) # random 0's and 1's of Size N

    #EbN0dB = np.arange(0,30,3) # Eb/N0 range in dB
    fc = 100 # carrier frequency in Hz
    OF = 8 # over sampling factor
    fs = OF*fc #sampling frequency
    L = 1 #samples in each symbol by default 1
    #snrdB = 15
    #BER = np.zeros(len(EbN0dB)) 
    #result = qpsk_mod(bits,fc,fs)
    #s = result['s(t)']
    
    
    #for items in s:
        
    if s.ndim==1:# if s is single dimensional vector
        P=L*sum(abs(s)**2)/len(s) #Actual power in the vector
    else: 
        P=L*sum(sum(abs(s)**2))/len(s) # power of the vector
    
    N0 = P/snrlin #spectral density of noise
    
    from numpy.random import standard_normal
    # n = np.sqrt(N0/2)*(standard_normal(s.shape)+1j*standard_normal(s.shape))
    
    
    n = math.sqrt(N0/2)*(standard_normal(s.shape)+1j*standard_normal(s.shape))
    r = s + n # received signal   
    
    # noise = dict()
    # noise['AWGN/Noise'] = r
    
    return r

#noise = AWGN()
#print AWGN(s,EbN0dB,N)
