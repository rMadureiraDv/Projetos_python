import customtkinter as ctk
import json
import tkinter as tk
from tkinter import messagebox

import json.scanner
carregador = []
#ctk window open---
ctk.set_appearance_mode("dark")
frame = ctk.CTk('#000000')
frame.maxsize(512,512)
frame.minsize(512,512)
#ctk window end ---
#binds
var = 0
listas = tk.Listbox(frame,font=("arial",20,"bold"),width=25,height=8)
listas.grid(row=0,column=0,padx=10,pady=310)
with open("storage.json") as fp:
    carregador = json.load(fp)
    for i in range(0,len(carregador),1):
        listas.insert(i,f"{carregador[i].get("nome")},{carregador[i].get("idade")},{carregador[i].get("tl")}")
entryF = ("arial",15,"bold")
entryC = "#000000"

#binds end
#functions
def adicionar ():
   
    
    nm = str(nome.get())
    idd = int(idade.get())
    tl = str(telefone.get())
    carregador.append({"nome" : nm,"idade" : idd,"tl" : tl})
    it = len(carregador)
    with open ("storage.json","w") as writter:
        json.dump(carregador, writter,indent= 4)
    listas.insert(it,f"{carregador[it-1].get("nome")},{carregador[it-1].get("idade")},{carregador[it-1].get("tl")}")

def remover ():
    selec = listas.curselection()
    l = selec[0]
    print(l)
    del carregador[l]
    with open("storage.json","w") as wr:
        json.dump(carregador,wr,indent= 4)
    listas.delete(l)
    
# functions end
#ctk objects
ctk.CTkLabel(frame,font=("arial",32,"bold"),text_color="#ffffff",text="JSON TEST").place(x=160,y=32)

nome = ctk.CTkEntry(frame,font= entryF,text_color=entryC,placeholder_text="NOME",fg_color="#ffffff",
                    bg_color="#000000",width=400,height=30)
nome.place(x = 32 , y = 92)

idade = ctk.CTkEntry(frame,font= entryF,text_color=entryC,placeholder_text="IDADE",fg_color="#ffffff",
                    bg_color="#000000",width=400,height=30)
idade.place(x = 32 , y = 122)

telefone = ctk.CTkEntry(frame,font= entryF,text_color=entryC,placeholder_text="TELEFONE",fg_color="#ffffff",
                    bg_color="#000000",width=400,height=30)
telefone.place(x = 32 , y = 152)

bt = ctk.CTkButton(frame,bg_color='#000000',fg_color='#3C6B08',text="adicionar",text_color="#ffffff",
                   command=adicionar)
bt.place(x = 64,y = 192)
bt = ctk.CTkButton(frame,bg_color='#000000',fg_color='#4F0304',text="remover",text_color="#ffffff",
                   command=remover)
bt.place(x = 320,y = 192)
#ctk objects end


frame.mainloop()