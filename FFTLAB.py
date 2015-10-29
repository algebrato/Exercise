#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def my_funtion(t):
    p = np.sin(t) + 2*np.sin(10*t)+10*np.sin(50*t)+3*np.sin(20*t) 
    return p

punti = 20

t = np.arange(punti)
x = (t*2*3.1415)/punti

freq = np.fft.fftfreq(t.shape[-1],d=1./punti)
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








