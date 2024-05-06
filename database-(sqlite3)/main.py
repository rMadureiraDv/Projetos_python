import sqlite3
import customtkinter as ctk
import tkinter as tk
#frame area----
conector = sqlite3.connect('data.db')
iterator = conector.cursor()
ctk.set_appearance_mode("system")
frame = ctk.CTk("#000000")
frame.minsize(512,512)
frame.maxsize(512,512)
frame.title("database demo")
frame.after(201, lambda :frame.iconbitmap("Assets\\icon.ico"))
#frame area end

#labels and entries set area ----

cFonte = '#757171'
fgEntry= '#D1C6C6'
fonteLabel = ('Arial',20,'bold')
fonteEntry = ('Arial',15,'bold')
entrywidth = 400
entryheight = 30

#labels and entries set area end

#funcitons area ----
def adicionar ():
    a = nome_pessoa.get()
    b = idade_pessoa.get()
    c = altura.get()
    
    addsql = 'INSERT INTO identidade (NOME, IDADE, ALTURA) VALUES (?, ?, ?)'
    iterator.execute(addsql,(a,b,c))
    conector.commit()
    nome_pessoa.delete(0,'end')
    idade_pessoa.delete(0,'end')
    altura.delete(0,'end')

#functions area end ----

#ctk objects area
ctk.CTkLabel(frame,font=('Arial',36,'bold'),text='DataBase v0.01',text_color=cFonte).place(x = 128 ,y = 32)

ctk.CTkLabel(frame,font=fonteLabel,text='NOME:',text_color=cFonte).place(x = 32 ,y = 128)

nome_pessoa = ctk.CTkEntry(frame,font=fonteEntry,fg_color=fgEntry,width=entrywidth,height=entryheight
                           ,text_color=cFonte)
nome_pessoa.place(x=32,y = 158)


ctk.CTkLabel(frame,font=fonteLabel,text='IDADE:',text_color=cFonte).place(x = 32 ,y = 256)

idade_pessoa = ctk.CTkEntry(frame,font=fonteEntry,fg_color=fgEntry,width=entrywidth,height=entryheight
                           ,text_color=cFonte)
idade_pessoa.place(x=32,y = 288)


ctk.CTkLabel(frame,font=fonteLabel,text='ALTURA',text_color=cFonte,bg_color="transparent")place(x = 32 ,y = 384)

altura = ctk.CTkEntry(frame,font=fonteEntry,fg_color=fgEntry,width=entrywidth,height=entryheight
                           ,text_color=cFonte)
altura.place(x=32,y = 414)

bt = ctk.CTkButton(frame,font=fonteLabel,text='ARMAZENAR',text_color='#999292',command=adicionar)
bt.place(x=168,y=458)

#ctk objects area end ----

frame.mainloop()
conector.close()
iterator.close()