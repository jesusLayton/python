archivo=open("agenda.txt","w")
lista=[]
opcion=0
nombres={""}
cedula={""}
telefono={""}
def Verlista (listado):
    global lista
    return lista
# def Listafiltrada (lista,datoabuscar):
#
#     return resultados
def datocompleto(completo): # me va abuscar en la lista de listas que tengo si el dato que le indico esta hay o cualquier coincidencia
    resultados=[] # guardo los datos en esta lista
    for lista in listadelistas: #
        if lista[0].lower()==(datocompleto): # endswith funciona para verificar si el texto o la palabra sea exactamente igual
            resultados.append(lista[0])
    return resultados
while opcion !=6:
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar Beneficiario")
    print("6. Salir")
    opcion=int(input())
    if opcion == 1:
        archivo=open("agenda.txt","a")
        listacompleta=Verlista(lista)
        print("Lista de beneficiaciorios:")
        print(*listacompleta,sep="\n")
    archivo.closed
    if opcion == 2:
        print("Digite la letra por la que empiezan los beneficiarios:")
        dato = input()

        resultados1 = []
        resultados2 = []
        contador = -1
        contador2 = -1
        name = []
        # for datos in lista:
        for g in range(0, len(lista), 3):
            name.append(lista[g])
        for datos in name:
            contador += 1
            if name[contador].startswith(dato):
                resultados1.append(datos)
        for k in lista:
            contador2 += 1
            if resultados1[0] == k:
                resultados2.append(k)
                resultados2.append(lista[contador2+1])
                resultados2.append(lista[contador2+2])
        print(resultados2)

        #print(Listafiltrada(lista,dato))
    archivo.closed
    if opcion == 3:
        archivo=open("agenda.txt","a")
        print("Digite la información del beneficiario a agregar:")
        nombres=input()
        lista.append(nombres)
        cedula = int(input())
        lista.append(cedula)
        telefono = int(input())
        lista.append(telefono)
        print("El beneficiario ha sido agregado al listado")
    archivo.closed
    if opcion == 4:
        print("Digite el nombre y apellido del beneficiario a buscar:")
        nombrecompleto=input()
        completo=datocompleto(nombrecompleto)
        print(completo)
    archivo.closed
    if opcion == 6:
        print("Hasta pronto")
print(lista)