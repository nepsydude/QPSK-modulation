# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:07:23 2020

@author: Prabesh
"""

def AWGN(s,SNRdB,L=1):
    import math
    from numpy.random import standard_normal
  
    gamma = 10**(SNRdB/10) #SNR to linear scale
    
    if s.ndim==1:# if s is single dimensional vector
        P=L*sum(abs(s)**2)/len(s) #Actual power in the vector
    else: # for multi-dimensional signals like MFSK
        P=L*sum(sum(abs(s)**2))/len(s) # if s is a matrix [MxN]
        
    N0=P/gamma #  noise spectral density    
    #if isrealobj(s):# check if input is real/complex object type
        # n = sqrt(N0/2)*standard_normal(s.shape) # computed noise
    # else:
    n = math.sqrt(N0/2)*(standard_normal(s.shape)+1j*standard_normal(s.shape))
    r = s + n # received signal    
    return r


