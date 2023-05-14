from tkinter import *
from PIL import ImageTk, Image

def change_image(event,label_clic):
    picture = Image.open('resources/pikachu.png')
    picture = picture.resize((76,106))
    imagen = ImageTk.PhotoImage(picture)
    label_clic.config(image=imagen)
    label_clic.image = imagen

def frame(ventana,n):
    frames = ['']*n
    for i in range(n):
        frames[i] = Frame(ventana)
        frames[i].pack(pady=10,padx=20)
    return frames

def imagen(img,n):
    n *= n
    images = ['']*n
    for i in range(n):
        images[i] = ImageTk.PhotoImage(img)
    return images

def label(frame, img, n):
    new_n = n*n
    labels = ['']*new_n
    for i in range(n):
        j = 0
        while j < n:
            k = (i*(n))+j
            labels[k] = Label(frame[i],image=img[k])
            labels[k].pack(side=LEFT)
            labels[k].bind("<Button-1>",lambda event, labeles = labels[k]: change_image(event, labeles))
            j += 1
    return labels