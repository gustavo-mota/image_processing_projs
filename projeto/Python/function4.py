from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2

from function2 import *
from function3 import conv_media
from function3 import filtro_conv
from function3 import conv_laplaciano

import numpy as np
import matplotlib.pyplot as plt
import cv2

def laplaciano(img, filtro, tamanho, fator_laplaciano):
	img2 = conv_laplaciano(img, filtro, tamanho)
	img2 = img2 * fator_laplaciano
	img2 = img + img2
	return img2

def high_boost(img, filtro, tamanho, fator_high_boost):
	img2 = conv_media(img, filtro, tamanho)
	mascara = img - img2
	return img + mascara * fator_high_boost

#path = "C:\\Users\\mateus\\Desktop\\image_processig\\imagens\\"
#path_image = "Fig0340(a)(dipxe_text).tif"
#imagem = import_img(path+path_image, None, True)
#print(imagem)
#mostrar_img(imagem)
#imagem2 = high_boost(imagem, "Media", 3, 4.5)
#mostrar_img2(imagem, imagem2, True)