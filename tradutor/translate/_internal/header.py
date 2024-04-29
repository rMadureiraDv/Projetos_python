from googletrans import Translator
from tkinter import ALL
from tkinter import messagebox

import customtkinter as ctk


ctk.set_appearance_mode("dark")
frame = ctk.CTk("#000000")
frame.title("TRADUTOR V1.0")
frame.minsize(512,512)
frame.maxsize(512,512)
fonte1 = '#7C7B8B'

valores = []
linguagens = ["---","ar","zh-cn","zh-tw","nl","eo","de","el","en","pt","es","ja"]
pTRad = {}
with open ('Languages.txt','r') as language:
        for x in language:
                x.split()
                str(valores.append(x))

for i in range (0,len(valores)):
            pTRad.update({valores[i]:linguagens[i]})
                


