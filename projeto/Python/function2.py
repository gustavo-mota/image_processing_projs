from function1 import mostrar_img
from function1 import import_img

import numpy as np
import matplotlib.pyplot as plt
import cv2


def histograma_imagem(img, plotar = False):
	histograma = [0]*256

	for i in range(len(img)):
		for j in range(len(img[0])):
			histograma[img[i][j][0]] += 1

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
	img2 = img*0

	for i in range(len(histograma_p)):
		if i == 0:
			histograma_p_acumulado[i] = histograma_p[i]
		else:
			histograma_p_acumulado[i] = histograma_p_acumulado[i-1]+histograma_p[i]

	histograma_novo = np.zeros(256)
	for i in range(0,256,1):
		histograma_novo[i] = np.ceil(histograma_p_acumulado[i]*255)

	for i in range(len(img)):
		for j in range(len(img[0])):
			img2[i][j] = histograma_novo[img[i][j]]

	if plotar:
		fig, axis = plt.subplots(1,2)
		axis[0].imshow(img)
		axis[1].imshow(img2)

	return img2

def fatiamento_bits(img, bit):
	img2 = img*0

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
	return img2
	
def esteganografia(img):
	lenght_message = img.shape[0]*img.shape[1]*img.shape[2]/8
	lenght_message = int(lenght_message)
	print("O número de caracteres disponíveis é de:", lenght_message)
	mensagem_bin = message(lenght_message)
	cont = 0

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
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
					return img
	return img

def ler_mensagem(img):
	mensagem_bin = ""
	mensagem_normal = ""
	n_caracteres = int(input("insira o número de caracteres: "))
	cont = 0
	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				if img[i][j][k]%2 == 0:
					mensagem_bin += "0"
				else:
					mensagem_bin += "1"
				cont +=1
	for i in range(0,n_caracteres*8,8):
		if mensagem_bin[i:i+8] == "00100000":
			mensagem_normal += " "
		else:
			mensagem_normal += chr(int(mensagem_bin[i:i+8], 2))
	return mensagem_normal

def message(lenght_message):
	mensagem = input("Insira a mensagem a ser compactada: ")
	while len(mensagem) > lenght_message:
		print("Mensagem muito grande, tente novamente.")
		mensagem = input("Insira a mensagem a ser compactada: ")
	mensagem_binaria = ""
	for i in range(len(mensagem)):
		if mensagem[i] == " ":
			mensagem_binaria += "00100000"
		else:
			mensagem_binaria += "0" + (bin(ord(mensagem[i])))[2::]
	return mensagem_binaria


#path = "C:\\Users\\mateus\\Desktop\\processamento_de_imagens\\imagens\\"
#path_image = "238.jpg"
#imagem = import_img(path+path_image, "cinza")

#mostrar_img(imagem)
#histo = histograma_imagem(imagem, True)
#imagem = equalizacao(imagem, histo, True)
#mostrar_img(imagem)
#imagem_bit = fatiamento_bits(imagem, 0)
#mostrar_img(imagem_bit)
#imagem_bit = fatiamento_bits(imagem, 7)
#mostrar_img(imagem_bit)
#imagem = esteganografia(imagem)
#mostrar_img(imagem)
#ler_mensagem(imagem)