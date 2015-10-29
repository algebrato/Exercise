#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import funct

    
def DO_FFT():
    Freq_campionamento = 5;
    punti = 51

    t = np.arange(punti)
    x = (t*2*3.1415)/Freq_campionamento+(t.shape[-1]*2*3.1415)/punti

    freq = np.fft.fftfreq(t.shape[-1],d=1./(Freq_campionamento) )
    S = np.fft.fft(funct.my_funct(x))
    F = np.abs(freq)
    A = np.abs(S*2/punti)

    plt.subplot(211)
    plt.plot(x,funct.my_funct(x),'bo',x, funct.my_funct(x),'k')

    plt.subplot(212)
    plt.plot(F,A,'bo',F,A,'k')

    dati_out = np.array([x,funct.my_funct(x)])

    plt.show()

if __name__ == '__main__':
    DO_FFT()


