from header import *
language = 0
#functions area -------------
def switch (choice):
        global language
        language = choice
def traducao ():
    TranslatedText.configure(state='normal')
    TranslatedText.delete(0,'end')

    lingua = str(pTRad.get(language))
    tTraduzir = str(textToTranslate.get())

    if (lingua == 'None'):
          messagebox.showerror("ERRO!!!","Escolha uma Lingua para Traduzir!!!")
          return -1
    elif (not tTraduzir):
          messagebox.showerror("ERRO!!","Digite uma palavra para traduzir")
          return -1
    leitura = Translator()
    TranslatedText.insert(0,leitura.translate(tTraduzir,src='auto',dest=lingua).text)
    TranslatedText.configure(state='disabled')  
#functions area end

#Ctk objects --------
ctk.CTkLabel(frame,font=("Arial",36,'bold'),text_color= fonte1,text='Tradutor V1.00').pack(pady= 20)

ctk.CTkLabel(frame,font=("Arial",25,'bold'),text_color= fonte1,text='DIGITE AQUI PARA TRADUZIR:').place(x= 25,y = 120)

textToTranslate = ctk.CTkEntry(frame,font=("Arial",15,'bold'),text_color= fonte1,width=450,height=25)
textToTranslate.place(x=25 , y= 150)

ctk.CTkLabel(frame,font=("Arial",25,'bold'),text_color= fonte1,text='TEXTO TRADUZIDO:').place(x= 25,y = 240)

TranslatedText = ctk.CTkEntry(frame,font=("Arial",15,'bold'),text_color= fonte1,width=450,height=25)
TranslatedText.place(x=25 , y= 270)
TranslatedText.configure(state='disabled')

options = ctk.CTkOptionMenu(frame,font=('Arial',12,'bold'),width=100,text_color='#000000',
                            bg_color='#000000',fg_color=fonte1,button_color=fonte1,values=valores,anchor='center',command=switch)
options.place(x=300,y=200)

btTraduzir = ctk.CTkButton(frame,width=150,height=30,text='TRADUZIR',fg_color=fonte1
                           ,bg_color='#000000',hover_color='#DBD2D2',command=traducao)
btTraduzir.place(x = 25 ,y = 200)

#ctk objects end------

frame.mainloop()