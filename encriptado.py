linea=input()
salto=""
mesaje=[]
fin=True
while fin:
    linea=input()
    if linea=="___________":
        break

    if linea=="|    o .o |":
        continue
    else:
        numero=linea
        numero=numero.replace("|","")
        numero=numero.replace(".","")
        numero=numero.replace(" ","0")
        numero=numero.replace("o","1")
        numero1=numero



        t = numero
        t = t[::-1]
        cuenta = 0
        for i in range(len(t)):
            if t[i] == '1':
                salida = 2 ** (i)
                cuenta = cuenta + salida

        if cuenta == 13:
            cuenta+=""
        else:
            caracter=chr(cuenta)


        salida+=caracter
    print(salida)


#         else:
#             caracter = chr(cuenta)
#             mesaje.append(caracter)
#
# mensaje = ''.join(mesaje)
# print(mensaje)

#print(mesaje)


