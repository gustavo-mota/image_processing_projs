from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2
from function1 import filtro_linear_multiplo

from function3 import conv_media
from function3 import filtro_conv

import numpy as np
import matplotlib.pyplot as plt
import cv2

"""
Parâmetros RGB: três matrizes de cinza com as intesidades de vermelho,
verde e azul.

Parâmetros HSV: variação de tipo da cor (H), da saturação (S) e intensidade (V)
"""
def HSV2RGB(pixel):
	H = pixel[0]
	S = pixel[1]
	V = pixel[2]
	# cor: array contendo uma cor no formato HSV
	# [tonalidade (0 - 360), saturação (0 - 1), brilho (0 - 1)]
	C = S * V
	m = V - C
	if 0 <= H <= 60:
		X = C * (H/60)
		return [(C+m), (X+m), (0+m)]
	elif H <= 120:
		X = C * (1 - (H - 60)/60)
		return [(X+m), (C+m), (0+m)]
	elif H <= 180:
		X = C * (H - 120)/60
		return [(0+m), (C+m), (X+m)]
	elif H <= 240:
		X = C * (1 - (H - 180)/60)
		return [(0+m), (X+m), (C+m)]
	elif H <= 300:
		X = C * (H - 240)/60
		return [(X+m), (0+m), (C+m)]
	else:
		X = C * (1 - (H - 300)/60)
		return [(C+m), (0+m), (X+m)]

def RGB2HSV(pixel):
	pixel[0] = int(pixel[0])
	pixel[1] = int(pixel[1])
	pixel[2] = int(pixel[2])
	V = int(pixel.max())/255
	if pixel.max() > 0:
		S = 1 - pixel.min()/pixel.max()
	else:
		S = 0
	if pixel[0] == pixel[1] and pixel[1] == pixel[2]:
		H = 0
	elif pixel[0] == pixel.max() and pixel[1] >= pixel[2]:
		H = int(60*(pixel[1] - pixel[2])/(pixel.max() - pixel.min()))
	elif pixel[0] == pixel.max() and pixel[1] <= pixel[2]:
		H = int(60*(pixel[1] - pixel[2])/(pixel.max() - pixel.min()) + 360)
	elif pixel[1] == pixel.max():
		H = int(60*(pixel[2] - pixel[0])/(pixel.max() - pixel.min()) + 120)
	else:
		H = int(60*(pixel[0] - pixel[1])/(pixel.max() - pixel.min()) + 240)

	return [H, S, V]

#######################################################

def RGB_HSV(img):
	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(img)):
		for j in range(len(img[0])):
				pixel_HSV = RGB2HSV(np.int_(img[i][j]))
				img2[i][j][0] = pixel_HSV[0]
				img2[i][j][1] = pixel_HSV[1]
				img2[i][j][2] = pixel_HSV[2]

	return (img2)

def HSV_RGB(img):
	img2 = np.zeros((img.shape[0], img.shape[1], 3))
	for i in range(len(img2)):
		for j in range(len(img[0])):
			for k in range(3):
				img2[i][j] = HSV2RGB(img[i][j])
	return img2




path = "C:\\Users\\mateus\\Desktop\\rotulacao\\imagens\\"
path_image = "531.jpg"
imagem = import_img(path+path_image, "cinza", False)
mostrar_img(imagem)
#imagem_HSV = RGB_HSV(imagem)
#imagem2 = HSV_RGB(imagem_HSV)
#imagem = np.double(imagem)/255
#imagem2 = filtro_linear_multiplo(imagem, [[0.30, 0], [0.30, 1], [0.5, 1], [0.5, 0.3], [0.6, 0.3], [0.6, 0], [1, 0]])
#mostrar_img2(imagem, imagem2)