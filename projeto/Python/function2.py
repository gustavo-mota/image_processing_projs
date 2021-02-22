from function1 import mostrar_img
from function1 import import_img
from function1 import mostrar_img2

import numpy as np
import matplotlib.pyplot as plt
import cv2


def histograma_imagem(img, plotar = False):

	img2 = np.int_(img*255)
	histograma = np.zeros(256)

	for i in range(len(img)):
		for j in range(len(img[0])):
			histograma[int(img2[i][j][0])] += 1

	if plotar:
		eixo = [i for i in range(0,256,1)]
		fig, axis = plt.subplots(2)
		axis[0].imshow(img)
		axis[1].bar(eixo, histograma)
		plt.xlim(0,255)
		plt.show()

	return histograma

def equalizacao(img, histograma, plotar = False):

	pixels = img.shape[0]*img.shape[1]

	histograma_p = np.array(histograma)/pixels
	histograma_p_acumulado = np.zeros(256)
	histograma_novo = np.zeros(256)

	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(histograma_p)):
		if i == 0:
			histograma_p_acumulado[i] = histograma_p[i]
		else:
			histograma_p_acumulado[i] = histograma_p_acumulado[i-1]+histograma_p[i]
	for i in range(0,256,1):
		histograma_novo[i] = np.rint(histograma_p_acumulado[i]*255)

	for i in range(len(img)):
		for j in range(len(img[0])):
			pixel = histograma_novo[int(img[i][j][0]*255)]/255
			img2[i][j] = [pixel, pixel, pixel]

	if plotar:
		eixo = [i for i in range(0,256,1)]
		fig, axis = plt.subplots(2,2)
		axis[0][0].imshow(img)
		axis[1][0].imshow(img2)
		axis[0][1].bar(eixo, histograma)
		axis[1][1].bar(eixo, histograma_imagem(img2))
		plt.show()

	return np.double(img2)

def fatiamento_bits(img, bit):
	img = np.int_(img*255)
	img2 = np.zeros((img.shape[0], img.shape[1], 3))

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				numero_bit = str(bin(img[i][j][k]))[2:]
				numero_bit = numero_bit[::-1]

				if len(numero_bit) >= (bit+1) and numero_bit[bit] == "0":
					img2[i][j][k] = 0
				elif len(numero_bit) >= (bit+1) and numero_bit[bit] != "0":
					img2[i][j][k] = 255
				else:
					img2[i][j][k] = 0
	return np.double(img2)/255
	
def esteganografia(img, mensagem):

	mensagem_bin = message(mensagem)
	cont = 0

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(img.shape[2]):
				if mensagem_bin[cont] == "0" and img[i][j][k]%2 == 0:
					pass
				elif mensagem_bin[cont] == "0" and img[i][j][k]%2 != 0:
					img[i][j][k] = img[i][j][k] - 1
				elif mensagem_bin[cont] == "1" and img[i][j][k]%2 != 0:
					pass
				else:
					img[i][j][k] = img[i][j][k] + 1
				cont += 1
				if cont == (len(mensagem_bin)):
					return np.double(img)/255
	return np.double(img)/255

def ler_mensagem(img, lenght_message):
	mensagem_bin = ""
	mensagem_normal = ""
	cont = 0
	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				if img[i][j][k]%2 == 0:
					mensagem_bin += "0"
				else:
					mensagem_bin += "1"
				cont +=1
	for i in range(0,lenght_message*8,8):
		if mensagem_bin[i:i+8] == "00100000":
			mensagem_normal += " "
		else:
			mensagem_normal += chr(int(mensagem_bin[i:i+8], 2))
	return mensagem_normal

def message(mensagem):

	mensagem_binaria = ""
	for i in range(len(mensagem)):
		if mensagem[i] == " ":
			mensagem_binaria += "00100000"
		else:
			mensagem_binaria += "0" + (bin(ord(mensagem[i])))[2::]
	return mensagem_binaria


#path = "C:\\Users\\mateus\\Desktop\\image_processig\\imagens\\"
#path_image = "Fig0326(a)(embedded_square_noisy_512).tif"
#imagem = import_img(path+path_image, None, True)

#mostrar_img(imagem)

#histo = histograma_imagem(imagem, True) 
#imagem2 = equalizacao(imagem, histo, True)


#imagem2 = fatiamento_bits(imagem, 7)
#mostrar_img(imagem_bit)
#imagem_bit = fatiamento_bits(imagem, 5)
#mostrar_img(imagem_bit)
#imagem = esteganografia(imagem)
#mostrar_img(imagem)
#ler_mensagem(imagem)
#mostrar_img2(imagem, imagem2, True)