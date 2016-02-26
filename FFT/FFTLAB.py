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



    print ("Sampling    = %s Hz" % Freq_campionamento)
    print ("#Points     = %s" % punti)
    peak=return_peak(F,A)
    print peak #non va.
    

    plt.subplot(211)
    plt.plot(x, y,'k',x,y,'bo')

    plt.subplot(212)
    plt.plot(F,A,'bo')

    plt.show()


def load_file(nome_file):
    try:
        dati = np.loadtxt(nome_file)
        print "Load data from file: "+nome_file
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror) 
        exit(7)

    x,y= dati[:,0], dati[:,1]
    return x,y

def return_peak(F,A):
    peak = np.array([]);
    massimo=0.
    
    for i in range(len(F)/2-1):
        if(abs(A[i+1]-A[i])> 1.3 ):
            massimo=A[i]
            if(A[i+1] > massimo):
                massimo=F[i+1]
                np.append(peak,[massimo])
            print massimo


    return peak








if __name__ == '__main__':
    print "FFT - build periodigram"
    print "Usage: ./FFTLAB.py [File]\n"
    n = len(sys.argv)
    if n < 2:
        print "Error: too few arguments"
        exit(1)
    if n > 2:
        print "Error: too many arguments"
        exit(2)
    
    x,y=load_file(sys.argv[1])
    DO_FFT(x,y)


