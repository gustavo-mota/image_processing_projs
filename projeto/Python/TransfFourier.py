from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2

from function3 import conv_media
from function3 import filtro_conv

import numpy as np
import matplotlib.pyplot as plt
import cv2

import matplotlib.colors as cl

import sys
sys.path.insert(1, '../Python')

from function1 import *

import time

def read_image(path, mod=0):
    BGR_im = cv2.imread(path, mod)
    RGB_img = cv2.cvtColor(BGR_im, cv2.COLOR_BGR2RGB)
    # corrigir esses nomes de variáveis
    if mod == 1:
        RGB_img = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)
    return RGB_img

def show_image(im, wk=0, name='image'):
    cv2.imshow(name, im, gray)
    cv2.waitKey(wk)
    cv2.destroyAllWindows()

def spatial2frequency(img2):
    '''
        img: imagem no domínio do espaço
        
        np array da imagem no domínio da frequência
    '''
    img = img2.copy()
    img_f = np.empty(img.shape, dtype=np.complex128)
    for i,j in zip(
                np.nditer(img_f, op_flags=['readwrite']),
                np.ndindex(img_f.shape)
                ):
            i = pixel2fourier(j, img)
    np.nditer.close
    return img_f

def pixel2fourier(coord, img):
    '''
        coord: tupla com coordenadas x,y do pixel que queremos
        img: imagem no domínio do espaço
    '''
    pixel_s = 0
    x, y = coord
    M, N = img.shape
    
    for m in np.ndindex(img.shape[0]):
        for n in np.ndindex(img.shape[1]): 
            pixel_s += \
            img[m[0], n[0]] * \
            np.exp( ( -2j * np.pi ) * \
                    ( ( (x*m[0])/M ) + ( (y*n[0])/N ) )
                  )
    np.nditer.close
    return pixel_s

def frequency2spatial(img):
    '''
        img: imagem no domínio da frequência
        
        np array no domínio espacial
    '''
    
    img_s = np.empty(img.shape, dtype=np.int8)
    
    for i,j in zip(
                np.nditer(img_s, op_flags=['readwrite']),
                np.ndindex(img_s.shape)
                ):
            i = fourier2pixel(j, img)
            #print(i)
    np.nditer.close
    print(img_s.dtype)
    return img_s

def fourier2pixel(coord, img):
    '''
        coord: tupla com coordenadas x,y do pixel que queremos
        img: imagem no domínio da frequência
    '''
    pixel_f = 0
    x, y = coord
    M, N = img.shape
    # debugar subtraindo img.shape por 1
    for m in np.ndindex(img.shape[0]):
        for n in np.ndindex(img.shape[1]): 
            pixel_f += \
            img[m[0], n[0]] * \
            np.exp( 2j * np.pi * ( (x*m[0])/M + (y*n[0])/N ) )
            print(np.exp( 2j * np.pi * ( (x*m[0])/M + (y*n[0])/N ) ))
    #pixel_f *= 1/(M*N)
    np.nditer.close
    return pixel_f

def ft_apply(img, filt):
    fft_img = np.fft.fft2(img)
    fft_img = np.fft.fftshift(fft_img)
    fft_img2 = np.abs(fft_img)
    mostrar_img(fft_img2)
    #fft_img *= filt
    fft_img = np.fft.ifftshift(fft_img)
    fft_img = np.fft.ifft2(fft_img)
    mostrar_img(np.abs(fft_img))

    return fft_img

#imagem = import_img("C:\\Users\\mateus\\Desktop\\rotulacao\\imagens\\imgf1.jpg", "RGB", True)
imagem = cv2.imread("C:\\Users\\mateus\\Desktop\\rotulacao\\imagens\\imgf1.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
mostrar_img(imagem, 1)
ft_apply(imagem, 1)

imagem_fourier = spatial2frequency(imagem)
mostrar_img(np.abs(imagem_fourier))
