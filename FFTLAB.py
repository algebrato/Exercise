#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def my_funtion(t):
    p = np.sin(t)+2*np.sin(2*t)+10*np.sin(4*t) 
    return p


Freq_campionamento = 10;
punti = 51

t = np.arange(punti)
x = (t*2*3.1415)/Freq_campionamento+(t.shape[-1]*2*3.1415)/punti

freq = np.fft.fftfreq(t.shape[-1],d=1./(Freq_campionamento) )
S = np.fft.fft(my_funtion(x))
F = np.abs(freq)
A = np.abs(S*2/punti)

plt.subplot(211)
plt.plot(x,my_funtion(x),'bo',x, my_funtion(x),'k')

plt.subplot(212)
plt.plot(F,A,'bo',F,A,'k')

dati_out = np.array([x,my_funtion(x)])


#for i in range(0,punti):
#    print dati_out[0][i],dati_out[1][i]




plt.show()








