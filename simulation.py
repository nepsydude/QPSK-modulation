# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:07:58 2020

@author: Prabesh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from modulation import qpsk_mod
from gausnoise import AWGN
from demodulation import qpsk_demodule


N = 100000 # Number of symbols to transmit
EbN0dB = np.arange(-4,11,2) # Eb/N0 range in dB
fc = 100 # carrier frequency in Hz
OF = 8 # over sampling factor
fs = OF*fc #sampling frequency
L = 2*OF #samples in each symbol
#snrdB = 30  
BER = np.zeros(len(EbN0dB)) 

bits = np.random.randint(2, size=N) # random 0's and 1's of Size N

result = qpsk_mod(bits,fc,fs)
s = result['s(t)']




for i, EbN0 in enumerate(EbN0dB):
    
    r = AWGN(s,N)
    bits_det = qpsk_demodule(r)
    BER[i] = np.sum(bits!=bits_det)/N
    
theoreticalBER = 0.5*erfc(np.sqrt(10**(EbN0dB/10)))
