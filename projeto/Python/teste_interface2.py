from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image, ImageTk


from function1 import * 


root = Tk()
root.title("Funções teste")
root.geometry("640x400")
root.configure(background = "#dde")

def comando():
	print("")
BarraDeMenu = Menu(root)
Menu_Arquivo = Menu(BarraDeMenu, tearoff = 0)
Menu_Arquivo.add_command(label = "mostrar imagem", command = comando)
Menu_Arquivo.add_command(label = "fechar", command = root.quit)
BarraDeMenu.add_cascade(label = "Arquivo", menu = Menu_Arquivo)
root.config(menu = BarraDeMenu)


root.mainloop()