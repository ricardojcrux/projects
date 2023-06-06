from tkinter import * 
from tkinter import messagebox

class Decimal(Tk):
    def __init__(self):
        super().__init__()
        self.title('Decimal to Roman Number')
        self.resizable(width=False,height=False)

        self.titulo = Label(self, text='Decimal to Roman Number', font=('Arial',20))
        self.titulo.pack(padx=10, pady=10)

        self.frame = Frame(self)
        self.frame.pack()

        self.decimal = Entry(self.frame, font=('Arial',15))
        self.decimal.pack(padx=10, side=LEFT)

        self.boton = Button(self.frame,text='Calculate', font=('Arial',12), command= lambda : self.dec_to_roman(self.decimal.get()))
        self.boton.pack(side=LEFT)

        self.number = Label(self, text='...', font=('Roman SD',30))
        self.number.pack(pady=10)

    def dec_to_roman(self, decimal):
        try:
            decimal = int(decimal)
            dicc = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
            roman = ''
            for value, numeral in dicc.items():
                while decimal >= value:
                    roman += numeral
                    decimal -= value
            self.number.config(text=roman)
        except ValueError:
            messagebox.showinfo(message='Inserte un año válido')
    
decimal = Decimal()
decimal.mainloop()