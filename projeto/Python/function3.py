from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2

import numpy as np
import matplotlib.pyplot as plt
import cv2

def conv_media(img, filter, tamanho):

	filtro, divisor = filtro_conv(filter, tamanho)
	valor_min = 0.0
	valor_max = 1.0


	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):

				matriz_n = np.zeros((tamanho,tamanho))

				n_x = int((1-tamanho)/2)

				for l in range(tamanho):
					n_y = int((1-tamanho)/2)
					for m in range(tamanho):
						if (j+n_y) >= 0 and (i+n_x) >=0 and (j+n_y) < len(img[0]) and (i+n_x)< len(img) :
							matriz_n[l][m] = img[i + n_x][j + n_y][k]
						n_y += 1
					n_x += 1

				matriz_f = filtro*matriz_n
				pixel = 0
				for l in range(len(matriz_f)):
					for m in range(len(matriz_f[0])):
						pixel += matriz_f[l][m]
				pixel = pixel/divisor
				if pixel < valor_min:
					valor_min = pixel
				elif pixel > valor_max:
					valor_max = pixel

				if img[i][j][0] == img[i][j][1] == img[i][j][2]:
					img2[i][j] = [pixel, pixel, pixel]
					break
				else:
					img2[i][j][k] = pixel
	return img2


def filtro_conv(filter, tamanho): 
	filtro = np.zeros((tamanho, tamanho))

	if filter == "Media":
		for i in range(tamanho):
			for j in range(tamanho):
				filtro[i][j] = 1
		divisor = tamanho**2

	elif filter == "Media_Ponderada":
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

	elif filter == "Generico":
		for i in range(tamanho):
			for j in range(tamanho):
				filtro[i][j] = float(input("Insira o valor [%d][%d] do filtro: ")%(i,j))
		divisor = 0
		for i in range(tamanho):
			for j in range(tamanho):
				divisor += filtro[i][j]

	elif filter == "Laplaciano":
		filtro = np.array([[0,1,0],
			[1,-4,1],
			[0,1,0]])
		divisor = 1
	elif filter == "Laplaciano_Diagonal":
		filtro = np.array([[1,1,1],
			[1,-8,1],
			[1,1,1]])
		divisor = 1
	elif filter == "Laplaciano_Inverso":
		filtro = np.array([[0,-1,0],
			[-1,4,-1],
			[0,-1,0]])
		divisor = 1
	elif filter == "Laplaciano_Diagonal_Inverso":
		filtro = np.array([[-1,-1,-1],
			[-1,8,-1],
			[-1,-1,-1]])
		divisor = 1
	elif filter == "Sobel_Dfx":
		filtro = np.array([
			[1, 0, -1],
			[2, 0, -2],
			[1, 0, -1]
					])

		divisor = 1

	elif filter == "Sobel_Dfy":
		filtro = np.array([
			[-1, -2, -1],
			[0, 0, 0],
			[1, 2, 1]
					])

		divisor = 1

	return (filtro, divisor)


def conv_mediana(img, tamanho):

	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):

				matriz_n = []

				n_x = int((1-tamanho)/2)

				for l in range(tamanho):
					n_y = int((1-tamanho)/2)
					for m in range(tamanho):
						if (j+n_y) >= 0 and (i+n_x) >=0 and (j+n_y) < len(img[0]) and (i+n_x)< len(img) :
							matriz_n.append(img[i + n_x][j + n_y][k])
						else:
							matriz_n.append(0)
						n_y += 1
					n_x += 1
				matriz_n.sort()
				pixel = matriz_n[int((tamanho**2+1)/2)]
				img2[i][j][k] = pixel

	return img2


def binarizacao(img, pixel = 127):

	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				if img[i][j][k] > pixel:
					img2[i][j][k] = 255

	return img2


def conv_sobel(img, tamanho):
	img_Dfx = conv_media(img, "Sobel_Dfx", tamanho)
	img_Dfy = conv_media(img, "Sobel_Dfy", tamanho)

	imagem = abs(img_Dfx) + abs(img_Dfy)

	valor_min = imagem.min()
	valor_max = imagem.max()

	imagem = (imagem - valor_min)/(valor_max - valor_min)

	return imagem

def conv_laplaciano(img, filter, tamanho):
	img2 = conv_media(img, filter, tamanho)
	return (img2 - img2.min())/(img2.max() - img2.min())

#path = "C:\\Users\\mateus\\Desktop\\image_processig\\imagens\\"
#path_image = "Fig0343(a)(skeleton_orig).tif"
#imagem = import_img(path+path_image, None, True)
#imagem = np.ones((5, 5, 3))

#mostrar_img(imagem)
#imagem2 = conv_media(imagem, "Media", 3) - ok
#imagem2 = conv_laplaciano(imagem, "Laplaciano", 3) - ok
#imagem2 = conv_mediana(imagem, 3) - ok
#imagem2 = conv_sobel(imagem, 3) - ok
#mostrar_img2(imagem, imagem2)



