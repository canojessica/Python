from tkinter import*
from tkinter import messagebox
import os
def get_calc ():
    os.system("calc")

def saludar():
    messagebox.showinfo(message= "¡hola, mundo!", title="saludo" )
   
ventana = Tk()
ventana.title("primera ventana")
ventana.iconbitmap("imagen/je.ico")
ventana.geometry("520x480")
ventana.config(bg="skyblue")
ventana.resizable(0,0)
boton = Button(text="abrir calculadora", command=get_calc)
boton.place(x=50, y =50)
boton = Button(text="saludo", command=saludar)
boton.place(x=100, y =100)
ventana.mainloop()
