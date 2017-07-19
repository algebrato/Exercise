#!/usr/bin/python

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage import data_dir
from skimage.transform import radon, rescale
from skimage.transform import iradon
from skimage.transform import iradon_sart


devstd_iter = np.array([])


image = imread("Rec3.png", as_grey=True)


theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta, circle=True)

reconstruction = iradon(sinogram, theta=theta, circle=True)
reconstruction_sart = iradon_sart(sinogram, theta=theta)
reconstruction_sart2 = iradon_sart(sinogram, theta=theta, image=reconstruction_sart)

e = reconstruction - image
print('Conversione analitica - errore: %.3g' % np.sqrt(np.mean(e**2)))

error = reconstruction_sart - image
print('Iterazione 1 - errore: %.3g' % np.sqrt(np.mean(error**2)))

devstd_iter=np.append(devstd_iter,np.sqrt(np.mean(error**2)))

for i in range(2,10):
    reconstruction_N = iradon_sart(sinogram, theta=theta, image=reconstruction_sart)
    error2 = reconstruction_N - image
    print('Iterazione %g - errore: %.3g' % (i, np.sqrt(np.mean(error2**2))) )
    reconstruction_sart = reconstruction_N
    devstd_iter=np.append(devstd_iter,np.sqrt(np.mean(error2**2)))


fig, axes = plt.subplots(2, 2, figsize=(8, 8.5), sharex=True, sharey=True,
                                 subplot_kw={'adjustable': 'box-forced'})






ax = axes.ravel()
ax[0].set_title("Ricostruzione Algoritmo Analitico",fontsize=10)
ax[0].imshow(reconstruction, cmap=plt.cm.Greys_r)

ax[1].set_title("Differenza Ricostruito-Originale",fontsize=10)
ax[1].imshow(reconstruction-image, cmap=plt.cm.Greys_r)

ax[2].set_title("Ricostruzione Algoritmo Iterativo N=6",fontsize=10)
ax[2].imshow(reconstruction_N, cmap=plt.cm.Greys_r)

ax[3].set_title("Differenza Ricostruito-Originale",fontsize=10)
ax[3].imshow(reconstruction_N-image, cmap=plt.cm.Greys_r)
plt.savefig('immagini.png')


plt.figure(2)
plt.title('DevStd vs Numero Iterazioni')
plt.xlabel('Numero di Step')
plt.ylabel('Dev.Std.')
plt.plot(devstd_iter,'bo',devstd_iter,'r--')
plt.savefig('devstd.png')












