#!/usr/bin/python

#default module
import numpy as np
import matplotlib.pyplot as plt
import sys
import string

#personal module
import funct

    
def DO_FFT(x,y):
    
    Freq_campionamento = 1./(x[1]-x[0])
    punti = y.shape[-1]

    t = np.arange(punti)
    freq = np.fft.fftfreq(t.shape[-1],d=1./(Freq_campionamento) )
    S = np.fft.fft(y)
    F = np.abs(freq)
    A = np.abs(S*2/punti)

    print ("Freq di campionamento = %s Hz" % Freq_campionamento)
    print ("Numero punti          = %s" % punti)

    

    plt.subplot(211)
    plt.plot(x, y,'k',x,y,'bo')

    plt.subplot(212)
    plt.plot(F,A,'bo',F,A,'k')

    plt.show()


def load_file(nome_file):
    dati = np.loadtxt(nome_file)
    x,y= dati[:,0], dati[:,1]
    return x,y


if __name__ == '__main__':
    n = len(sys.argv)
    if n < 2:
        print "Err < 2"
        quit()
    if n > 2:
        print "Err > 2"
        quit()
    
    x,y=load_file(sys.argv[1])
    DO_FFT(x,y)


