"""
Name : Demineur
Author : Eliott, Chakib
"""
from tkinter import *
import tkinter.font as tkFont
from demineur import *

root = Tk() # Création de la fenêtre

def quit():
    root.destroy()
root.bind('<Escape>',lambda e: quit())

# Configuration de la fenêtre
root.title('Demineur')
root.geometry('600x600')
root.resizable(False,False)

# Polices d'écriture
Title_font = tkFont.Font(family='Trebuchet MS', size=18, weight='bold')

titre = Label(text="Démineur !", font=Title_font).place(x=300,y=25,anchor='center')

root.mainloop()