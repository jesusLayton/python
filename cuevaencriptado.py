t=[65, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110, 32, 102, 111, 120, 32, 106, 117, 109, 112, 115, 32, 111, 118, 101, 114, 32, 116, 104, 101, 32, 108, 97, 122, 121, 32, 100, 111, 103, 46, 10]
g=len(t)
mesaje=[]
for i in range(43):
    caracter = chr(int(t[i]))
    mesaje.insert(g, caracter)

mensaje=''.join(mesaje)
print(mensaje)
