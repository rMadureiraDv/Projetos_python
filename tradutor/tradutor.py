from googletrans import Translator
import customtkinter as ctk

def traducao ():
    traduzido.delete(0,'end')
    trad = traduzir.get()
    trans = Translator()
    traduzido.insert(0,trans.translate(trad,dest='pt',src='auto').text)

    
ctk.set_appearance_mode('system')
frame = ctk.CTk('#000000')
frame.geometry('512x512')
frame.title("Tradutor mais feio ever")

ctk.CTkLabel(frame,text="Tradutor v0.069",font=('Arial',32,'bold'),text_color='#ffffff').pack(pady=20)

ctk.CTkLabel(frame,text="Digite aqui a frase pra traduzir",font=('Arial',20,'bold'),text_color='#ffffff').pack(pady=10)
traduzir = ctk.CTkEntry(frame,placeholder_text="Aqui",text_color='white',width=500)
traduzir.pack()

bt = ctk.CTkButton(frame,text='Traduzir',width=250,fg_color='white',text_color='#000000', command=traducao).pack(pady=20)

traduzido=ctk.CTkEntry(frame,text_color="white",width=500)
traduzido.pack(pady=30)

frame.mainloop()