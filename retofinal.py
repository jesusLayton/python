archivoreto=open("datosreto.txt","w")
datos=[]

for i in range(3):
    nombre=input().lower()
    cedula=input()
    numero=input()
    archivoreto.writelines(nombre+"\n")
    archivoreto.writelines(cedula+"\n")
    archivoreto.writelines(numero+"\n")
archivoreto.close()






ordenas la informacion de archivo y agruparlo en lista de listas
archivoreto=open("datosreto.txt","r")
lineas=archivoreto.readlines()
salida=[]
for linea in lineas:
    salida.append(linea.replace("\n",""))
listaordenada=[salida[i:i + 3] for i in range(0, len(salida), 3)]
print(listaordenada)


buscar=input().lower()
#buscar usuario con su nombre
for i in listaordenada:
    for k in i:
        if k==buscar:
            print(i[1])
            print(i[2])
archivoreto.close()


agregar un usuario al arichivo

ordenar los datos en una lista

archivoreto=open("datosreto.txt","r")
lineas=archivoreto.readlines()

listaordenada=[]
salida=[]
for linea in lineas:
    salida.append(linea.replace("\n",""))
    listaordenada=[salida[i:i + 3] for i in range(0, len(salida), 3)]
print(listaordenada)
#despues de que tenga la lista ordenada, se realiza la comparacion de las cedula
#si estan repetidas, no se puede escribir el nuevo usiario
archivoreto=open("datosreto.txt","a")
print("ingrese un nuevo usuario")

cuenta=0
while True:
    nombre = input().lower()
    cedula = input()
    numero = input()
    for i in listaordenada:
        for k in i:

            if k==cedula:
                print("ingresar otro numero de cedula, ese ya existe")
                cuenta=1
                break

        if cuenta==1:
            break

    if cuenta == 1:
        continue
    else:
        break


archivoreto.writelines(nombre+"\n")
archivoreto.writelines(cedula+"\n")
archivoreto.writelines(numero+"\n")
print("usuario ingresado con exito")
archivoreto.close()

borrar a un usuario


archivoreto=open("datosreto.txt","r")

lineas=archivoreto.readlines()
salida=[]
for linea in lineas:
    salida.append(linea.replace("\n",""))
listaordenada=[salida[i:i + 3] for i in range(0, len(salida), 3)]
print(listaordenada)

cel=input()

for i in listaordenada:
    for k in i:
        if k==cel:
            listaordenada.remove(i)
print(listaordenada)

archivoreto=open("datosreto.txt","w")


for i in listaordenada:
    for k in i:
        archivoreto.write(str(k)+"\n")
archivoreto.close()

