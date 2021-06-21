from tkinter import *
from tkinter import messagebox

def ventanaemergente():
    messagebox.showinfo("informacion","soy una ventana de info")
    messagebox.showwarning("advertencia", "soy una ventana de advertencia")
    messagebox.showerror("ERROR")
ventana=Tk()
ventana.title("mi primera ventana")
ventana.geometry("800x600")
texto=Label(
    text="soy una etiqueta de texto",
    fg="orange",
    font=("Dancing Script",20,"bold")
)
texto.pack()

boton=Button(
    text="dame clik",
    fg="white",
    bg="#9c3006",
    font=("Arial", 20, "bold"),
    command=ventanaemergente

)
boton.pack()

cuadrodetexto=Text(
    height=3,
    width=10
)
cuadrodetexto.pack()
#ventana.attributes('-fullscreen', True)
ventana.mainloop()
