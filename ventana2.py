from tkinter import *

estructura=[
    ["paula","rosado"],
    ["carolina","azul"],
    ["brayam","rojo"],
    ["jeniffer","azul"],
    ["jorge","rojo"],
    ["marcela","salmon"],
    ["alfonso","azul"]
]
totalfilas=len(estructura)
totalcolumnas=len(estructura[0])

ventanaest=Tk()

for fila in range(totalfilas):
    for columna in range(totalcolumnas):
        celda=Entry(
            width=20,
            fg="#9c0303",
            font=("Calibri",15,"bold italic")
        )
        celda.grid(row=fila,column=columna)
        celda.insert(END,estructura[fila][columna])

ventanaest.mainloop()