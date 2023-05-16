from tkinter import *
from PIL import ImageTk, Image
import os, random

def behind_image(event,label_clic):
    pass

def imagen():
    picture = Image.open('resources/backcard.png')
    picture = picture.resize((144,204))  
    return ImageTk.PhotoImage(picture)

def label(ventana, img, n):
    new_n = n*n
    labels = ['']*new_n
    for i in range(n):
        j = 0
        while j < n:
            k = (i*(n))+j
            labels[k] = Label(ventana,image=img)
            labels[k].grid(row=i,column=j)
            labels[k].bind("<Button-1>",lambda event, labeles = labels[k]: behind_image(event, labeles))
            j += 1
    return labels

def final_cards(cards):
    cards = [Image.open(f'resources/{card}') for card in cards]
    cards = [card.resize((144,204)) for card in cards]
    final_list = [ImageTk.PhotoImage(card) for card in cards]
    return final_list

def random_cards():
    cards = os.listdir('resources')
    cards.remove('backcard.png')
    cards = cards[:8]
    cards += cards
    random.shuffle(cards)
    final_card = final_cards(cards)
    return final_card

def behind_label(ventana, img, n):
    new_n = n*n
    labels = ['']*new_n
    for i in range(n):
        j = 0
        while j < n:
            k = (i*(n))+j
            labels[k] = Label(ventana,image=img[k])
            labels[k].grid(row=i,column=j)
            labels[k].bind("<Button-1>",lambda event, labeles = labels[k]: behind_image(event, labeles))
            j += 1
    return labels