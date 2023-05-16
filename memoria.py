from tkinter import *
from controller import *
from PIL import Image

memoria = Tk()
memoria.title('Juego de Parejas')
memoria.resizable(height=False, width=False)

a = 4

images = imagen()
labels = label(memoria,images, a)
cards = random_cards()
behind = behind_label(memoria,cards,a)

memoria.mainloop()