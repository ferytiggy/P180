# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:08:59 2024

@author: Aidan
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("P180")
root.geometry("600x600")
root.config(bg="green")

titulo = Label(root, text="Traductor De Idiomas", bg="green")
titulo.place(relx=0.5, rely=0.1, anchor=CENTER)
ingresar_texto = Label(root, text="Ingresar texto", bg="green")
ingresar_texto.place(relx=0.02, rely=0.2, anchor=w)
area_de_texto = Text(root, bg="green", height=5, wrap, width=100, padx=10, pady=10, bd)
area_de_texto.place(relx=0.02, rely=0.5, anchor=w)

root.mainloop()