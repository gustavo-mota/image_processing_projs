import numpy as np
import matplotlib.pyplot as plt
import cv2

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
		axis[0].imshow(img1)
		axis[1].imshow(img2)
	else:
		axis[0].imshow(img1, cmap = "gray", vmin = 0,vmax = 255)
		axis[1].imshow(img2, cmap = "gray", vmin = 0,vmax = 255)

	plt.show()

def import_img(path, padrao_cor = None):

	img = cv2.imread(path)
	if padrao_cor == "cinza":
		return img
	elif padrao_cor == "RGB":
		return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	else:
		return img

def negativo(img):
	# retorna o negativo da imagem
	return 255-img

def logaritmo(img, fator_L):
	# fator_L -> representa o número para multiplicar
	# o resultado, clareando ou escurecendo a imagem
	return np.int_(np.log((img/255)+1)*255*fator_L)

def correcao_gama(img, fator_g):
	# A correção de gama usa uma função exponencial
	# fator_g é o exponencial da imagem f(x,y) = i(x,y)^fator_g
	return np.int_(((img/255)**fator_g)*255)

def filtro_linear_binario(img, fator_linear):
	#fator linear: abaixo desse valor, os pixels são zerados.
	img2 = img*0

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				if img[i][j][k] < fator_linear:
					img2[i][j] = [0,0,0]
				else:
					img2[i][j] = [255,255,255]
	return img2

def filtro_linear_simples(img, fator_a, fator_b):
	# fator_a: coeficiente angular da reta
	# fator_b: coeficiente linear da reta
	# dominio: região de controle, onde o primeiro item da lista
	# é o valor mínimo e o segundo item é o valor máximo
	img2 = img*0

	for i in range(len(img)):
		for j in range(len(img[0])):
			for k in range(3):
				pixel = img[i][j][k]*fator_a + fator_b
				img2[i][j][k] = pixel

	return img2

def filtro_linear_multiplo(img, c_fatores, dominio):
	# conjunto de fatores: lista contendo os coeficientes lineares.
	# dominio: regiões das equações lineares.
	img2 = img *0
	for i in range(len(dominio)):
		for j in range(len(img)):
			for k in range(len(img[0])):
				for m in range(3):
					if img[j][k][m] >= dominio[i][0] and img[j][k][m] < dominio[i][1]:

						pixel = img[j][k][m]*c_fatores[i][0] + c_fatores[i][1]
						img2[j][k][m]= int(pixel)	

	return img2


#path = "C:\\Users\\mateus\\Desktop\\processamento_de_imagens\\imagens\\"
#path_image = "49.jpg"
#imagem = import_img(path+path_image, "RGB")

#mostrar_img(imagem)
#imagem2 = negativo(imagem)
#imagem2 = logaritmo(imagem, 2)
#imagem2 = correcao_gama(imagem, 2)
#imagem2 = filtro_linear_binario(imagem, 127)
#imagem2 = filtro_linear_simples(imagem, 2, -80)
#imagem = filtro_linear_multiplo(imagem, [[1,0],[0,0]], [[0,125],[125,255]])
#mostrar_img2(imagem, imagem2)