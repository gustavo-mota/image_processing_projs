from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image, ImageTk


from function1 import *
from function2 import * 
from function3 import *
from function4 import *
from function6 import *
class App_I:
    def __init__(self, master=None):

    	self.frame1 = Frame(master)
    	self.frame1.pack()

    	self.local_imagem = Frame(master)
    	self.local_imagem.pack()

    	#self.imagem = self.import_img(path+path_image, "RGB", True)

##############################################################################
    def import_img(self, path, root, padrao_cor = None, normalizacao = True):
    	img = cv2.imread(path)
    	if padrao_cor == "cinza":
    		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    		img = RGB2GRAY(img, "Med")
    	elif padrao_cor == "RGB":
    		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    	if normalizacao:
    		self.imagem = np.double(img)/255
    	else:
    		self.imagem = img

    	root.title(path)

    	self.Canvas(root, width=300, height=300)
    	image = Image.open(path)
    	image = image.resize((300,120))
    	image = ImageTk.PhotoImage(image)

    	self.create_image(0, 0, anchor=NW, image=image)
    	self.pack()

    	#root.configure(background = )

    def modificar_imagem(self, img):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()    	

    	self.img_temp = img

    	self.mensagem1 = Label(self.opcao_1, text = "Deseja salvar a modificação? ")
    	self.mensagem1.pack()

    	self.botao_sim = Button(self.opcao_1)
    	self.botao_sim["text"] = "sim"
    	self.botao_sim["command"] = lambda: self.modif_1(self)
    	self.botao_sim.pack()

    	self.botao_nao = Button(self.opcao_1)
    	self.botao_nao["text"] = "não"
    	self.botao_nao["command"] = lambda: self.opcao_1.destroy()
    	self.botao_nao.pack()

    def modif_1(self):
    	self.imagem = self.img_temp
    	self.opcao_1.destroy()

    def mostrar_imagem(self, img):
    	color = "teste"
    	plotagem = plt.figure(figsize = (5,5))

    	if color == "cinza":
        	plotagem = plt.imshow(img, cmap = "gray", vmin = 0,vmax = 255)
    	else:
        	plotagem = plt.imshow(img, cmap = "gray")
    	plt.show()

##############################################################################
    def negativo(self):
    	img = self.imagem
    	img2 = negativo(img)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def log_1(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira a constante de logaritimo")
    	self.mensagem1.pack(side = LEFT)

    	self.const_log = Entry(self.opcao_1)
    	self.const_log.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.log_2(self)
    	self.botao_2.pack()

    def log_2(self):
    	const_log = float(self.const_log.get())
    	self.opcao_1.destroy()
    	img = self.imagem
    	img2 = logaritmo(img, const_log)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def gama_1(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.opcao_2 = Frame()
    	self.opcao_2.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira a constante de exponecial")
    	self.mensagem1.pack(side = LEFT)
    	self.mensagem2 = Label(self.opcao_2, text = "Insira a constante de linear")
    	self.mensagem2.pack(side = LEFT)

    	self.const_expo = Entry(self.opcao_1)
    	self.const_expo.pack()

    	self.const_m = Entry(self.opcao_2)
    	self.const_m.pack()

    	self.botao_2 = Button(self.opcao_2)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.gama_2(self)
    	self.botao_2.pack()

    def gama_2(self):
    	const_expo = float(self.const_expo.get())
    	const_m = float(self.const_m.get())

    	self.opcao_1.destroy()
    	self.opcao_2.destroy()

    	img = self.imagem
    	img2 = correcao_gama(img, const_m, const_expo)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def linear_1(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira o número de pontos da sua função: ")
    	self.mensagem1.pack(side = LEFT)

    	self.const_n = Entry(self.opcao_1)
    	self.const_n.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.linear_2(self)
    	self.botao_2.pack()

    def linear_2(self):
    	self.const_numeros = int(self.const_n.get())
    	self.pontos = []
    	self.func = []

    	self.opcao_2 = Frame()
    	self.opcao_2.pack()

    	self.opcao_3 = Frame()
    	self.opcao_3.pack()

    	self.opcao_4 = Frame()
    	self.opcao_4.pack()

    	self.mensagem1 = Label(self.opcao_2, text = "Insira a coordenada X (original da imagem)")
    	self.mensagem1.pack()

    	self.const_x = Entry(self.opcao_2)
    	self.const_x.pack()

    	self.mensagem2 = Label(self.opcao_2, text = "Insira a coordenada Y (ou constante)")
    	self.mensagem2.pack(side = LEFT)

    	self.const_y = Entry(self.opcao_2)
    	self.const_y.pack()

    	self.botao_2 = Button(self.opcao_3)
    	self.botao_2["text"] = "linear"
    	self.botao_2["command"] = lambda: self.linear_3(self, "l")
    	self.botao_2.pack(side = LEFT)

    	self.botao_3 = Button(self.opcao_3)
    	self.botao_3["text"] = "logaritmo"
    	self.botao_3["command"] = lambda: self.linear_3(self, "log")
    	self.botao_3.pack(side = LEFT)

    	self.botao_4 = Button(self.opcao_3)
    	self.botao_4["text"] = "negativo"
    	self.botao_4["command"] = lambda: self.linear_3(self, "n")
    	self.botao_4.pack(side = LEFT)

    	self.botao_5 = Button(self.opcao_3)
    	self.botao_5["text"] = "gama"
    	self.botao_5["command"] = lambda: self.linear_3(self, "g")
    	self.botao_5.pack(side = LEFT)

    def linear_3(self, funcao):
    	f_logaritima = 1
    	f_gama = 1
    	self.coord_X = float(self.const_x.get())/255
    	self.coord_Y = float(self.const_y.get())/255

    	self.pontos.append([self.coord_X, self.coord_Y])
    	self.func.append(funcao)

    	if funcao == "log":
    		f_logaritima = self.coord_Y*255
    	elif funcao == "g":
    		f_gama = self.coord_Y*255


    	if self.const_numeros == 1:
    		self.opcao_1.destroy()
    		self.opcao_2.destroy()
    		self.opcao_3.destroy()
    		self.opcao_4.destroy()

    		self.const_log = 0
    		self.const_g = 0


    		img = self.imagem
    		img3 = linear_partes(img, self.pontos, self.func, "c",f_logaritima, f_gama)
    		self.mostrar_imagem(self, img3)
    		self.modificar_imagem(self, img3)

    	else:
    		self.const_numeros -= 1
    		self.mensagem3 = Label(self.opcao_4, text = "Ponto cadastrado com sucesso.")
    		self.mensagem3.pack()

    def binarizacao_1(self):

    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira o pixel para limiarização")
    	self.mensagem1.pack(side = LEFT)

    	self.fator_binario = Entry(self.opcao_1)
    	self.fator_binario.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.binarizacao_2(self)
    	self.botao_2.pack()

    def binarizacao_2(self):

    	f_binario = int(self.fator_binario.get())

    	self.opcao_1.destroy()

    	img2 = limiarizacao(self.imagem, f_binario)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)


##############################################################################
    def histograma(self):
    	histograma_imagem(self.imagem, True)

    def histograma_RGB(self):
    	histograma_R = histograma_RGB(self.imagem, 0)
    	histograma_G = histograma_RGB(self.imagem, 1)
    	histograma_B = histograma_RGB(self.imagem, 2)
    	imagem_hsv = RGB_HSV(np.int_(self.imagem*255))
    	histograma_V = histograma_RGB(imagem_hsv, 2)

    	fig, ax = plt.subplots(2,2)
    	eixo = [i for i in range(0,256,1)]
    	ax[0][0].bar(eixo, histograma_R, color ="red")
    	ax[0][0].set_title("Histograma Vermelho")
    	ax[0][1].bar(eixo, histograma_G, color = "green")
    	ax[0][1].set_title("Histograma Verde")
    	ax[1][0].bar(eixo, histograma_B, color = "blue")
    	ax[1][0].set_title("Histograma Azul")
    	ax[1][1].bar(eixo, histograma_V, color = "black")
    	ax[1][1].set_title("Histograma Intensidade")
    	plt.show()

    def equalizar_cinza(self):
    	histograma = histograma_imagem(self.imagem)
    	img2 = equalizacao(self.imagem, histograma, True)
    	self.modificar_imagem(self, img2)

    def equalizar_cor(self, cor):
    	if cor == "R":
    		color = 0
    	elif cor == "G":
    		color = 1
    	else:
    		color = 2
    	if cor == "V":
    		img = RGB_HSV(np.int_(self.imagem*255))
    		img2 = img.copy()
    		histograma = histograma_RGB(img, color)
    		img3 = equalizacao_cor(img2, histograma, color)
    		img3 = HSV_RGB(img3)
    		self.mostrar_imagem(self, img3)
    		self.modificar_imagem(self, img3)
    	else:
    		histograma = histograma_RGB(self.imagem, color)
    		img2 = equalizacao_cor(self.imagem, histograma, color)
    		self.mostrar_imagem(self, img2)
    		self.modificar_imagem(self, img2)

##############################################################################
    def convolucao_1(self, filtro):

    	try:
    		self.const_d = self.fator_2.get()
    	except:
    		self.cons_d = 1
    	try:
    		self.opcao_1.destroy()
    	except:
    		pass

    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "insira o tamanho do filtro")
    	self.mensagem1.pack(side = LEFT)

    	self.tamanho_filtro = Entry(self.opcao_1)
    	self.tamanho_filtro.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.convolucao_3(self, filtro)
    	self.botao_2.pack()

    def convolucao_2(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Selecione o filtro")
    	self.mensagem1.pack(side = LEFT)

    	self.botao_1 = Button(self.opcao_1)
    	self.botao_1["text"] = "Laplaciano"
    	self.botao_1["command"] = lambda: self.convolucao_1(self, "Laplaciano")
    	self.botao_1.pack(side = LEFT)

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "Laplaciano diagonal"
    	self.botao_2["command"] = lambda: self.convolucao_1(self, "Laplaciano_Diagonal")
    	self.botao_2.pack(side = LEFT)

    	self.botao_3 = Button(self.opcao_1)
    	self.botao_3["text"] = "Laplaciano inverso"
    	self.botao_3["command"] = lambda: self.convolucao_1(self, "Laplaciano_Inverso")
    	self.botao_3.pack(side = LEFT)

    	self.botao_4 = Button(self.opcao_1)
    	self.botao_4["text"] = "Laplaciano inverso diagonal"
    	self.botao_4["command"] = lambda: self.convolucao_1(self, "Laplaciano_Diagonal_Inverso")
    	self.botao_4.pack(side = LEFT)

    def convolucao_3(self, filtro):

    	t_fi = int(self.tamanho_filtro.get())

    	self.opcao_1.destroy()

    	if filtro == "Mediana":
    		img2 = conv_mediana(self.imagem, t_fi)
    	elif filtro == "Sobel":
    		img2 = conv_sobel(self.imagem, t_fi)
    	elif filtro == "High_Boost":
    		img2 = high_boost(self.imagem, "Media", t_fi, float(self.const_d))
    	elif filtro == "laplac":
    		img2 = laplaciano(self.imagem, "Laplaciano", t_fi, float(self.const_d))
    	else:
    		img2 = conv_media(self.imagem, filtro, t_fi)

    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def convolucao_4(self, filtro):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "insira o fator")
    	self.mensagem1.pack(side = LEFT)

    	self.fator_2 = Entry(self.opcao_1)
    	self.fator_2.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.convolucao_1(self, filtro)
    	self.botao_2.pack()



##############################################################################
    def RGB2Cinza(self, media):
    	img2 = RGB2GRAY(self.imagem, media)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def RGB2HSV(self):
    	img2 = RGB_HSV(np.int_(self.imagem*255))
    	self.modificar_imagem(self, img2)

    def HSV2RGB(self):
    	img2 = HSV_RGB(self.imagem)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def RGB2CYMK(self):
    	img2 = RGB2CMYK(self.imagem)
    	self.modificar_imagem(self, img2)

    def CYMK2RGB(self):
    	img2 = CMYK2RGB(self.imagem)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

#############################################################################
    def sepia(self):
    	img2 = sepia(self.imagem)
    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

    def chroma_Key_1(self):

    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.opcao_2 = Frame()
    	self.opcao_2.pack()

    	self.opcao_3 = Frame()
    	self.opcao_3.pack()

    	self.opcao_4 = Frame()
    	self.opcao_4.pack()

    	self.opcao_5 = Frame()
    	self.opcao_5.pack()

    	self.opcao_6 = Frame()
    	self.opcao_6.pack()

    	self.opcao_7 = Frame()
    	self.opcao_7.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira o espaço mínimo de verde")
    	self.mensagem1.pack(side = LEFT)

    	self.mensagem2 = Label(self.opcao_2, text = "Insira a intensidade mínima da saturação")
    	self.mensagem2.pack(side = LEFT)

    	self.mensagem3 = Label(self.opcao_3, text = "Insira a intensidade mínima da luminancia")
    	self.mensagem3.pack(side = LEFT)

    	self.mensagem4 = Label(self.opcao_4, text = "Insira o espaço máxima de verde")
    	self.mensagem4.pack(side = LEFT)

    	self.mensagem5 = Label(self.opcao_5, text = "Insira a intensidade máxima da saturação")
    	self.mensagem5.pack(side = LEFT)

    	self.mensagem6 = Label(self.opcao_6, text = "Insira a intensidade máxima da luminancia")
    	self.mensagem6.pack(side = LEFT)

    	self.mensagem7 = Label(self.opcao_7, text = "Insira a imagem para substituir")
    	self.mensagem7.pack(side = LEFT)

    	self.verde_min = Entry(self.opcao_1)
    	self.verde_min.pack()

    	self.saturacao_min = Entry(self.opcao_2)
    	self.saturacao_min.pack()

    	self.luminancia_min = Entry(self.opcao_3)
    	self.luminancia_min.pack()

    	self.verde_max = Entry(self.opcao_4)
    	self.verde_max.pack()

    	self.saturacao_max = Entry(self.opcao_5)
    	self.saturacao_max.pack()

    	self.luminancia_max = Entry(self.opcao_6)
    	self.luminancia_max.pack()

    	self.local_imagem = Entry(self.opcao_7)
    	self.local_imagem.pack()

    	self.botao_2 = Button(self.opcao_7)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.chroma_Key_2(self)
    	self.botao_2.pack()

    def chroma_Key_2(self):

    	verde_min = int(self.verde_min.get())
    	verde_max = int(self.verde_max.get())

    	saturacao_min = float(self.saturacao_min.get())
    	saturacao_max = float(self.saturacao_max.get())

    	luminancia_min = float(self.luminancia_min.get())
    	luminancia_max = float(self.luminancia_max.get())

    	local_imagem = str(self.local_imagem.get())

    	self.opcao_1.destroy()
    	self.opcao_2.destroy()
    	self.opcao_3.destroy()
    	self.opcao_4.destroy()
    	self.opcao_5.destroy()
    	self.opcao_6.destroy()
    	self.opcao_7.destroy()

    	img_entrada = import_img(path+"215.jpg", "RGB", True)
    	img_entrada = RGB_HSV(np.int_(img_entrada*255))

    	imagem_2 = RGB_HSV(np.int_(self.imagem*255))

    	for i in range(imagem_2.shape[0]):
    		for j in range(imagem_2.shape[1]):
    			valor1 = imagem_2[i][j][0] >= verde_min and imagem_2[i][j][0] <= verde_max
    			valor2 = imagem_2[i][j][1] >= saturacao_min and imagem_2[i][j][1] <= saturacao_max
    			valor3 = imagem_2[i][j][2] >= luminancia_min and imagem_2[i][j][2] <= luminancia_max

    			if valor1 and valor2 and valor3:
    				imagem_2[i][j] = img_entrada[i][j]

    	img2 = HSV_RGB(imagem_2)

    	self.mostrar_imagem(self, img2)
    	self.modificar_imagem(self, img2)

##############################################################################
    def Codificar_Mensagem_1(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	tamanho_mensagem = str((self.imagem.shape[0]*self.imagem.shape[1]*self.imagem.shape[2])/8)
    	texto1 = "O número de caracteres disponíveis é: " + tamanho_mensagem
    	self.mensagem1 = Label(self.opcao_1, text = texto1)
    	self.mensagem1.pack()
    	self.mensagem2 = Label(self.opcao_1, text = "Insira a mensagem a ser codificada")
    	self.mensagem2.pack(side = LEFT)

    	self.mensagem = Entry(self.opcao_1)
    	self.mensagem.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.Codificar_Mensagem_2(self)
    	self.botao_2.pack()

    def Codificar_Mensagem_2(self):
    	mensagem = self.mensagem.get()

    	self.opcao_1.destroy()

    	self.imagem = esteganografia(np.int_(self.imagem*255), mensagem)

    def Decodificar_Mensagem_1(self):
    	self.opcao_1 = Frame()
    	self.opcao_1.pack()

    	self.mensagem1 = Label(self.opcao_1, text = "Insira o tamanho da mensagem")
    	self.mensagem1.pack(side = LEFT)

    	self.mensagem = Entry(self.opcao_1)
    	self.mensagem.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.Decodificar_Mensagem_2(self)
    	self.botao_2.pack()

    def Decodificar_Mensagem_2(self):

    	tamanho_mensagem = int(self.mensagem.get())
    	mensagem = ler_mensagem(np.int_(self.imagem*255), tamanho_mensagem)
    	self.opcao_2 = Frame()
    	self.opcao_2.pack()

    	self.mensagem2 = Label(self.opcao_1, text = mensagem)
    	self.mensagem2.pack()

    	self.botao_2 = Button(self.opcao_1)
    	self.botao_2["text"] = "ok"
    	self.botao_2["command"] = lambda: self.Decodificar_Mensagem_3(self)
    	self.botao_2.pack()

    def Decodificar_Mensagem_3(self):
    	self.opcao_1.destroy()
    	self.opcao_2.destroy()














    	


path = "E:\\Documentos\\GitHub\\image_processing2\\projeto\\imagens\\"
path_image = "Fig0314(a)(100-dollars).tif"

root = Tk()
root.title("Funções teste")
root.geometry("640x400")
root.configure(background = "#dde") # !!!

App_I(root)

def funcao():
	pass

BarraDeMenu = Menu(root)
Menu_Arquivo = Menu(BarraDeMenu, tearoff = 0)
Menu_Arquivo.add_command(label = "abrir imagem", command = lambda: App_I.import_img(App_I, path+path_image, root, "RGB", True))
Menu_Arquivo.add_command(label = "salvar imagem", command = lambda: App_I.mostrar_imagem(App_I, App_I.imagem))
Menu_Arquivo.add_command(label = "fechar", command = root.quit)
BarraDeMenu.add_cascade(label = "Arquivo", menu = Menu_Arquivo)

Menu_funcoes = Menu(BarraDeMenu, tearoff = 0)
Menu_funcoes.add_command(label = "Negativo", command = lambda: App_I.negativo(App_I))
Menu_funcoes.add_command(label = "logaritmo", command = lambda: App_I.log_1(App_I))
Menu_funcoes.add_command(label = "gama_1", command = lambda: App_I.gama_1(App_I))
Menu_funcoes.add_command(label = "Função por partes", command = lambda: App_I.linear_1(App_I))
Menu_funcoes.add_command(label = "binarizacao", command = lambda: App_I.binarizacao_1(App_I))
BarraDeMenu.add_cascade(label = "Funções", menu = Menu_funcoes)

Menu_histograma = Menu(BarraDeMenu, tearoff = 0)
Menu_histograma.add_command(label = "Histograma", command = lambda: App_I.histograma(App_I))
Menu_histograma.add_command(label = "Histograma_cores", command = lambda: App_I.histograma_RGB(App_I))
Menu_histograma.add_command(label = "Equalização em cinza", command = lambda: App_I.equalizar_cinza(App_I))
Menu_histograma.add_command(label = "Equalização em vermelho", command = lambda: App_I.equalizar_cor(App_I, "R"))
Menu_histograma.add_command(label = "Equalização em azul", command = lambda: App_I.equalizar_cor(App_I, "G" ))
Menu_histograma.add_command(label = "Equalização em verde", command = lambda: App_I.equalizar_cor(App_I, "B" ))
Menu_histograma.add_command(label = "Equalização em intensidade", command = lambda: App_I.equalizar_cor(App_I, "V"))
BarraDeMenu.add_cascade(label = "normalizacao", menu = Menu_histograma)

Menu_convolucao = Menu(BarraDeMenu, tearoff = 0)
Menu_convolucao.add_command(label = "Média", command = lambda: App_I.convolucao_1(App_I, "Media"))
Menu_convolucao.add_command(label = "Média Ponderada", command = lambda: App_I.convolucao_1(App_I, "Media_Ponderada"))
Menu_convolucao.add_command(label = "Mediana", command = lambda: App_I.convolucao_1(App_I, "Mediana"))
Menu_convolucao.add_command(label = "High Boost", command = lambda: App_I.convolucao_4(App_I, "High_Boost"))
Menu_convolucao.add_separator()
Menu_convolucao.add_command(label = "Laplaciano", command = lambda: App_I.convolucao_2(App_I))
Menu_convolucao.add_command(label = "Mascara Laplaciano", command = lambda: App_I.convolucao_4(App_I, "laplac"))
Menu_convolucao.add_separator()
Menu_convolucao.add_command(label = "Sobel X", command = lambda: App_I.convolucao_1(App_I, "Sobel_Dfx"))
Menu_convolucao.add_command(label = "Sobel Y", command = lambda: App_I.convolucao_1(App_I, "Sobel_Dfy"))
Menu_convolucao.add_command(label = "Sobel", command = lambda: App_I.convolucao_1(App_I, "Sobel"))
Menu_convolucao.add_command(label = "Genérico", command = lambda: App_I.convolucao_1(App_I, "Generico"))
BarraDeMenu.add_cascade(label = "Filtros Espaciais", menu = Menu_convolucao)

Menu_cor = Menu(BarraDeMenu, tearoff = 0)
Menu_cor.add_command(label = "RGB -> HSV", command = lambda: App_I.RGB2HSV(App_I))
Menu_cor.add_command(label = "RGB -> YCMK", command = lambda: App_I.RGB2CYMK(App_I))
Menu_cor.add_command(label = "RGB -> GRAY1", command = lambda: App_I.RGB2Cinza(App_I, "Med"))
Menu_cor.add_command(label = "RGB -> GRAY2", command = lambda: App_I.RGB2Cinza(App_I, "Med_P"))
Menu_cor.add_separator()
Menu_cor.add_command(label = "HSV -> RGB", command = lambda: App_I.HSV2RGB(App_I))
Menu_cor.add_command(label = "YCMK -> RGB", command = lambda: App_I.CYMK2RGB(App_I))
BarraDeMenu.add_cascade(label = "Cor", menu = Menu_cor)

Menu_cores = Menu(BarraDeMenu, tearoff = 0)
Menu_cores.add_command(label = "Negativo", command = lambda: funcao)
Menu_cores.add_command(label = "logaritmo", command = lambda: funcao)
Menu_cores.add_command(label = "linear", command = lambda: funcao)
Menu_cores.add_command(label = "gama", command = lambda: funcao)
BarraDeMenu.add_cascade(label = "Modificação por Cores", menu = Menu_cores)

Menu_modificadores = Menu(BarraDeMenu, tearoff = 0)
Menu_modificadores.add_command(label = "Sepia", command = lambda: App_I.sepia(App_I))
Menu_modificadores.add_command(label = "Chroma Key", command = lambda: App_I.chroma_Key_1(App_I))
Menu_modificadores.add_command(label = "Codificar Mensagem", command = lambda: App_I.Codificar_Mensagem_1(App_I))
Menu_modificadores.add_command(label = "Descodificar Mensagem", command = lambda: App_I.Decodificar_Mensagem_1(App_I))
BarraDeMenu.add_cascade(label = "Modificadores", menu = Menu_modificadores)



root.config(menu = BarraDeMenu)


root.mainloop()