from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2
from function1 import filtro_linear_multiplo
from function1 import HSV_RGB
from function1 import RGB_HSV
from function1 import RGB2GRAY
from function2 import equalizacao

from function3 import conv_media
from function3 import filtro_conv

import numpy as np
import matplotlib.pyplot as plt
import cv2

def histograma_RGB(img, cor, plotar = False):
	histograma = np.zeros(256)
	img2 = np.int_(img.copy()*255)

	for i in range(len(img)):
		for j in range(len(img[0])):
			histograma[int(img2[i][j][cor])] += 1

	if plotar:
		eixo = [i for i in range(0,256,1)]
		fig, axis = plt.subplots(2)
		axis[0].imshow(img)
		axis[1].bar(eixo, histograma)
		plt.xlim(0,255)
		plt.show()

	return histograma

def equalizacao_cor(img, histograma, cor, plotar = False):

	pixels = img.shape[0]*img.shape[1]

	histograma_p = np.array(histograma)/pixels
	histograma_p_acumulado = np.zeros(256)
	histograma_novo = np.zeros(256)

	img2 = img.copy()

	for i in range(len(histograma_p)):
		if i == 0:
			histograma_p_acumulado[i] = histograma_p[i]
		else:
			histograma_p_acumulado[i] = histograma_p_acumulado[i-1]+histograma_p[i]
	for i in range(0,256,1):
		histograma_novo[i] = np.rint(histograma_p_acumulado[i]*255)
	for i in range(len(img)):
		for j in range(len(img[0])):
			pixel = histograma_novo[int(img[i][j][cor]*255)]/255
			img2[i][j][cor] = pixel

	if plotar:
		eixo = [i for i in range(0,256,1)]
		fig, axis = plt.subplots(2,2)
		axis[0][0].imshow(img)
		axis[1][0].imshow(img2)
		axis[0][1].bar(eixo, histograma)
		axis[1][1].bar(eixo, histograma_RGB(img2, cor))
		plt.show()

	return img2

def selecao_cor(img_HSV, H, S, V, rot = True):
	img = img_HSV.copy()
	# H = dominio entre 0 e 360
	# S = saturacao entre 0 e 1
	# V = luminancia entre 0 e 1

	H1 = np.array([H[0], H[1]])
	S1 = np.array([S[0], S[1]])
	V1 = np.array([V[0], V[1]])

	if rot:
		for i in range(img_HSV.shape[0]):
			for j in range(img_HSV.shape[1]):
				if H1.max() - H1.min() >= 180:
					valor1 = img[i][j][0] <= H1.min() or img[i][j][0] >= H1.max()
				else:
					valor1 = img[i][j][0] >= H1.min() and img[i][j][0] <= H1.max()

				valor2 = img[i][j][1] >= S1.min() and img[i][j][1] <= S1.max()
				valor3 = img[i][j][2] >= S1.min() and img[i][j][2] <= S1.max()

				if not(valor1) or not(valor2) or not(valor3):
					img[i][j][2] = 0
	else:
		for i in range(img_HSV.shape[0]):
			for j in range(img_HSV.shape[1]):
				if H1.max() - H1.min() >= 180:
					valor1 = img[i][j][0] <= H1.min() or img[i][j][0] >= H1.max()
				else:
					valor1 = img[i][j][0] >= H1.min() and img[i][j][0] <= H1.max()

				valor2 = img[i][j][1] >= S1.min() and img[i][j][1] <= S1.max()
				valor3 = img[i][j][2] >= S1.min() and img[i][j][2] <= S1.max()

				if (valor1) and (valor2) and (valor3):
					img[i][j][2] = 0


	return img

def chromakey(img_fundo, img_HSV):
	verde_B = int(input("Insira o menor valor de verde: "))
	verde_A = int(input("Insira o maior valor de verde: "))

	saturacao_B = int(input("Insira o menor valor de saturação: "))
	saturacao_A = int(input("Insira o maior valor de saturação: "))

	luminancia_B = int(input("Insira o menor valor de luminancia: "))
	luminancia_A = int(input("Insira o maior valor de luminancia: "))

	for i in range(img_fundo.shape[0]):
			for j in range(img_fundo.shape[1]):
				valor1 = img_fundo[i][j][0] >= verde_B and img_fundo[i][j][0] <= verde_A
				valor2 = img_fundo[i][j][1] >= saturacao_B and img_fundo[i][j][1] <= saturacao_A
				valor3 = img_fundo[i][j][2] >= luminancia_B and img_fundo[i][j][2] <= luminancia_A

				if valor1 and valor2 and valor3:
					img_fundo[i][j] = img_HSV[i][j]

	return img_fundo

def sepia(img):
	img_cinza = RGB2GRAY(img, "Med")
	for i in range(img_cinza.shape[0]):
		for j in range(img_cinza.shape[1]):
			if img_cinza[i][j][0] == 0:
				img_cinza[i][j][0] = 0.3
			elif img_cinza[i][j][0] >= 0.7:
				img_cinza[i][j][0] = 1
			else:
				img_cinza[i][j][0] = img_cinza[i][j][0] + 0.3

			if img_cinza[i][j][1] == 0:
				img_cinza[i][j][1] = 0.3
			elif img_cinza[i][j][1] >= 0.7:
				img_cinza[i][j][1] = 1
			else:
				img_cinza[i][j][1] = img_cinza[i][j][1] + 0.3

	return (img_cinza)

def variacao_matiz(img, variacao):

	img2 = img.copy()

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):

			img2[i][j][0] = img[i][j][0] + variacao
			if img2[i][j][0] >= 360:
				img2[i][j][0] -= 360
			elif img[i][j][0] < 0:
				img2[i][j][0] += 360

	return img2

def variacao_intensidade(img, variacao):

	img2 = img.copy()

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):

			img2[i][j][1] = img[i][j][1] + img[i][j][1]*variacao/100
			if img2[i][j][1] >= 1:
				img2[i][j][1] = 1
			elif img[i][j][1] < 0:
				img2[i][j][1] = 0

	return img2

def variacao_luminancia(img, variacao):

	img2 = img.copy()

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):

			img2[i][j][2] = img[i][j][2] + img[i][j][2]*variacao/100
			if img2[i][j][2] >= 1:
				img2[i][j][2] = 1
			elif img[i][j][2] < 0:
				img2[i][j][2] = 0
				
	return img2


#path = "C:\\Users\\mateus\\Desktop\\image_processig\\imagens\\"
#path_image = "348.jpg"
#imagem = import_img(path+path_image, "RGB")
#imagem_HSV = RGB_HSV(imagem)
#imagem_HSV2 = RGB_HSV(imagem2)
#mostrar_img(imagem)
#imagem_HSV3 = chromakey(imagem_HSV1, imagem_HSV2)
#imagem2 = HSV_RGB(imagem_HSV3)
#imagem_HSV = RGB_HSV(imagem)
#imagem_HSV2 = selecao_cor(imagem_HSV, [60, 140], [0, 1], [0, 1])
#imagem2 = HSV_RGB(imagem_HSV2)
#mostrar_img2(imagem, imagem2)
#histograma1 = histograma_RGB(imagem_HSV, 2, True)
#imagem_HSV2 = equalizacao_cor(imagem_HSV, histograma1, 2, True)
#imagem2 = np.int_(HSV_RGB(np.double(imagem_HSV2))*255)
#imagem2 = RGB2GRAY(imagem, "Med")
#mostrar_img(imagem2)
#imagem2 = sepia(imagem)
#mostrar_img2(imagem, imagem2)
#histograma_RGB(imagem, 0, True)
#histograma_RGB(imagem, 1, True)
#histograma_RGB(imagem, 2, True)
#mostrar_img2(imagem, imagem2)
