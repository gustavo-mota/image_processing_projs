import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import img_as_float

<<<<<<< HEAD
"""
Primeiro conjunto de funções:

Conjunto mais básico de funções, incluem 3 funções de vizualização
- mostrar_img(imagem, título, padrão de cor)
- mostrar_img2(imagem 1, imagem 2, normalização: caso seja verdadeiro, joga a escala para
padrão entre 0 e 1, se falso, coloca os valores abaixo de 0 para 0 e valores acima de 255
para 255)
- import_img(imagem e tipo de cor)

Funções de ajuste de cores:
- Negativo (imagem)
retorna o negativo da imagem
- logarítimo (imagem, falor de multiplicação da função)
retorna um pixel após ser submetido a uma escala logarítmica
- correcao_gama(imagem e fator gama) retorna uma função a^n, onde a é o
valor do pixel e n é o fator gama.
- filtro_linear_binario(img, fator linear): binarização, diferen para imagens coloridas
"""


##############
def mostrar_img(img, title = None,color = None, normalize=None):
	# Responsável por mostrar a imagem
	# O título deve ser o nome da imagem?
	# Color= padrão de cor, deve ser normatizado

    plt.figure(figsize = (5,5))
    if title != None:
    	plt.title(title)
    if color == "cinza":
        plt.imshow(img, cmap = "gray",norm=normalize vmin = 0,vmax = 255)
    else:
        plt.imshow(img, norm=normalize)
    plt.show()

def mostrar_img2(img1, img2, normatizado = False):
	fig, axis = plt.subplots(1, 2)
	if normatizado:
		axis[0].imshow(img1, cmap = "gray")
		axis[1].imshow(img2, cmap = "gray")
	else:
		axis[0].imshow(img1, cmap = "gray", vmin = 0,vmax = 255)
		axis[1].imshow(img2, cmap = "gray", vmin = 0,vmax = 255)

	plt.show()

def import_img(path, padrao_cor = None, normalizacao = True):

	img = cv2.imread(path)

	if padrao_cor == "cinza":
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img = RGB2GRAY(img, "Med")
	elif padrao_cor == "RGB":
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	if normalizacao:
		return np.double(img)/255
	else:
		return img

############################################################
def RGB2GRAY(img, f_l):
	img = np.int_(img*255)
	img2 = np.zeros((img.shape[0], img.shape[1], img.shape[2]))
	if f_l == "Med":
		for i in range(len(img)):
			for j in range(len(img[0])):

				pixel = int((float(img[i][j][0]) + float(img[i][j][0]) + float(img[i][j][0]))/3)
				img2[i][j] = [pixel, pixel, pixel]

	elif f_l == "Med_P":
		for i in range(len(img)):
			for j in range(len(img[0])):

				pixel = int(0.299*float(img[i][j][0])
				 + 0.587*float(img[i][j][1])
				 + 0.114*float(img[i][j][2]))

				img2[i][j] = [pixel, pixel, pixel]
	return np.double(img2)/255

def RGB2CMYK(img):
	img2 = np.zeros((img.shape[0],img.shape[1], img.shape[2]+1))
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			k = 1 - img[i][j].max()
			if k == 1:
				c = 0
				m = 0
				y = 0
			else:
				c = (1-img[i][j][0] - k)/(1 - k)
				m = (1-img[i][j][1] - k)/(1 - k)
				y = (1-img[i][j][2] - k)/(1 - k)

			img2[i][j][0] = c
			img2[i][j][1] = m
			img2[i][j][2] = y
			img2[i][j][3] = k

	return img2

def CMYK2RGB(img):
	img2 = np.zeros((img.shape[0], img.shape[1], img.shape[2] - 1))
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			img2[i][j][0] = (1-img[i][j][0])*(1 - img[i][j][3])
			img2[i][j][1] = (1-img[i][j][1])*(1 - img[i][j][3])
			img2[i][j][2] = (1-img[i][j][2])*(1 - img[i][j][3])

	return img2

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
####################################################################
def negativo(img):
	# img: array da imagem - double (0.0 a 1.0)
	# retorna o negativo da imagem
	return 1-img

def logaritmo(img, fator_L):
	# img: array da imagem - double (0.0 a 1.0)
	# fator_L: constante de multiplicação
	return (np.log(img + 1))*fator_L

def correcao_gama(img, fator_a, fator_g):
	# img: array da imagem - double (0.0 a 1.0)
	# fator_g: razão exponencial (float entre 0.0 e inf.)
	# fator_a: constante de multiplicação
	return fator_a*img**fator_g

def limiarizacao(img, fator_linear):
	# img: array da imagem - double (0.0 a 1.0)
	#fator linear: pixel para binarização - int (0 a 255)
	fator_linear = fator_linear/255
	img2 = np.zeros((img.shape[0], img.shape[1], img.shape[2]))

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				if img[i][j][k] < fator_linear:
					img2[i][j][k] = 0
				else:
					img2[i][j][k] = 1

	return img2

###################################################################
def filtro_linear_simples(img, fator_a, fator_b):
	#img: array da imagem - double (0.0 a 1.0)
	# fator_a: coeficiente angular da reta - float
	# fator_b: coeficiente linear da reta
	# dominio: região de controle, onde o primeiro item da lista
	# é o valor mínimo e o segundo item é o valor máximo
	img2 = np.zeros((img.shape[0], img.shape[1], img.shape[2]))

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				pixel = img[i][j][k]*fator_a + fator_b
				img2[i][j][k] = pixel

	return img2

def filtro_linear_multiplo(img, dominio):
	#img: array da imagem - double (0.0 a 1.0)
	# conjunto de fatores: lista contendo os coeficientes lineares.
	# dominio: regiões das equações lineares.
	ponto_i = [0,0]

	img2 = np.zeros((img.shape[0], img.shape[1], img.shape[2]))
	for i in range(len(dominio)):
		for j in range(img.shape[0]):
			for k in range(img.shape[1]):
				for m in range(img.shape[2]):
					if img[j][k][m] >= ponto_i[0] and img[j][k][m] <= dominio[i][0]:
						pixel = img[j][k][m]*coef_a + coef_b
						img2[j][k][m]= pixel

		ponto_i = dominio[i]
	return img2

def coeficientes_linear(ponto_A, ponto_B):
	if ponto_B[0] - ponto_A[0] == 0:
		coef_a = 0
		coef_b = ponto_B[1]
	else:
		coef_a = (ponto_B[1] - ponto_A[1])/(ponto_B[0] - ponto_A[0])
	coef_b = (ponto_A[1] - coef_a * ponto_A[0])

	return (coef_a, coef_b)

def linear_partes(img, pontos, funcoes, cor, f_log, f_g):
	#img - imagem
	#pontos - [[x1,y1],...[xn,yn]]
	#funcoes - n - negativa, log - logaritima,

	ponto_i = [0,0]
	img2 = img.copy()

	if cor == "c" or cor == "r":
		color = 0
	elif cor == "g":
		color = 1
	elif cor == "b" or color == "v":
		color = 2

	for i in range(len(pontos)):

		if funcoes[i] == "l":
			coef_a, coef_b = coeficientes_linear(ponto_i, pontos[i])
		for j in range(img.shape[0]):
			for k in range(img.shape[1]):
				if ponto_i[0] <= img[i][j][color] and img[i][j][color] <= pontos[i][0]:
					if funcoes[i] == "n":
						pixel = (1 - img[j][k][color])

					elif funcoes[i] == "log":
						pixel = (np.log(img[j][k][color] + 1)*f_Log)

					elif funcoes[i] == "l":
						pixel = coef_a *img[j][k][color] + coef_b

					elif funcoes[i] == "g":
						pixel = img[j][k][color]**f_g

					else:
						pixel = img[j][k][color]
					if cor == "c":
						img2[j][k] = [pixel, pixel, pixel]
					else:
						img2[j][k][color] = pixel

		ponto_i = pontos[i]

	return img2


