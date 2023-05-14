from tkinter import *
from controller import *
from PIL import ImageTk, Image

memoria = Tk()
memoria.title('Juego de Parejas')
memoria.resizable(height=False, width=False)

a = 4

picture = Image.open('resources/backcard.png')
picture = picture.resize((76,106))

frames = frame(memoria,a)
images = imagen(picture,a)
labels = label(frames,images, a)

memoria.mainloop()