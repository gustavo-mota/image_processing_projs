from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2

import numpy as np
import matplotlib.pyplot as plt
import cv2

def conv_media(img, filter, tamanho):

	filtro, divisor = filtro_conv(filter, tamanho)
	matriz_n = np.zeros((tamanho, tamanho))

	img2 = img*0

	for i in range(len(img)):
		for j in range(len(img[0])):
			for a in range(3):

				matriz_n = np.zeros((tamanho,tamanho))

				n_x = int((1-tamanho)/2)

				for k in range(tamanho):
					n_y = int((1-tamanho)/2)
					for m in range(tamanho):
						if (j+n_y) >= 0 and (i+n_x) >=0 and (j+n_y) < len(img[0]) and (i+n_x)< len(img) :
							matriz_n[k][m] = img[i + n_x][j + n_y][a]
						n_y += 1
					n_x += 1

				matriz_f = filtro*matriz_n
				pixel = 0
				for k in range(len(matriz_f)):
					for m in range(len(matriz_f[0])):
						pixel += matriz_f[k][m]
				pixel = int(pixel/divisor)
				img2[i][j][a] = pixel
	return img2


def filtro_conv(filter, tamanho): 
	filtro = np.zeros((tamanho, tamanho))

	if filter == "media":
		for i in range(tamanho):
			for j in range(tamanho):
				filtro[i][j] = 1
		divisor = tamanho**2

	elif filter == "media_ponderada":
		fator = 1
		for i in range(tamanho):
			for j in range(tamanho):
				filtro[i][j] = fator
				if j < (tamanho-1)/2:
					fator = fator*2
				else:
					fator = fator/2
			if i < (tamanho-1)/2:
				fator = fator*4
		divisor = 0
		for i in range(tamanho):
			for j in range(tamanho):
				divisor += filtro[i][j]
	elif filter == "generico":
		for i in range(tamanho):
			for j in range(tamanho):
				filtro[i][j] = float(input("Insira o valor [%d][%d] do filtro: ")%(i,j))
		divisor = 0
		for i in range(tamanho):
			for j in range(tamanho):
				divisor += filtro[i][j]
	elif filter == "laplaciano":
		filtro = np.array([[0,1,0],
			[1,-4,1],
			[0,1,0]])
		divisor = 1

	elif filter == "laplaciano_diagonal":
		filtro = np.array([[1,1,1],
			[1,-8,1],
			[1,1,1]])
		divisor = 1

	elif filter == "laplaciano_inverso":
		filtro = np.array([[0,-1,0],
			[-1,4,-1],
			[0,-1,0]])
		divisor = 1
	elif filter == "laplaciano_diagonal_inverso":
		filtro = np.array([[-1,-1,-1],
			[-1,8,-1],
			[-1,-1,-1]])
	elif filter == "Sobel":
		filtro = (
			np.array([
			[-1, 0, 1],
			[-2, 0, 2],
			[-1, 0, 1]
					]),
			np.array([
				[-1, -2, -1],
				[0, 0, ],
				[1, 2, 1]
			])
			)
		divisor = 1
	return (filtro, divisor)


def conv_mediana(img, tamanho):

	img2 = img*0

	for i in range(len(img)):
		for j in range(len(img[0])):
			for a in range(3):

				matriz_n = []

				n_x = int((1-tamanho)/2)

				for k in range(tamanho):
					n_y = int((1-tamanho)/2)
					for m in range(tamanho):
						if (j+n_y) >= 0 and (i+n_x) >=0 and (j+n_y) < len(img[0]) and (i+n_x)< len(img) :
							matriz_n.append(img[i + n_x][j + n_y][a])
						else:
							matriz_n.append(0)
						n_y += 1
					n_x += 1
				matriz_n.sort()
				pixel = matriz_n[int((tamanho**2+1)/2)]
				img2[i][j][a] = pixel

	return img2


def binarizacao(img, pixel = 127):

	img2 = img*0
	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				if img[i][j][k] > pixel:
					img2[i][j][k] = 255

	return img2




path = "C:\\Users\\mateus\\Desktop\\processamento_de_imagens\\imagens\\"
path_image = "Fig0312(a)(kidney).tif"
imagem = import_img(path+path_image, "RGB")
mostrar_img(imagem)
#imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
imagem2 = conv_media(imagem, "laplaciano_diagonal", 3)
mostrar_img2(imagem, imagem2, True)
#mostrar_img2(imagem, imagem+imagem2, True)
#imagem2 = conv_mediana(imagem2,3)
#mostrar_img2(imagem, imagem2)

