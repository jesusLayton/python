from os import  path
if not path.exists("agenda.txt"):
    archivoreto = open("agenda.txt", "w").close()
def datosenlista():
    archivoreto=open("agenda.txt", "r")
    lineas = archivoreto.readlines()
    archivoreto.close()
    listaordenada = []
    salida = []
    for linea in lineas:
        salida.append(linea.replace("\n", ""))
        listaordenada = [salida[i:i + 3] for i in range(0, len(salida), 3)]
    return listaordenada
def agregar1(nombre, cedula, numero):
    archivoreto = open("agenda.txt", "a")
    archivoreto.writelines(nombre + "\n")
    archivoreto.writelines(cedula + "\n")
    archivoreto.writelines(numero + "\n")
    archivoreto.close()
def agregar12(nombre, cedula, numero, lineas):
    cuenta1=0
    for i in lineas:
        for k in i:
            if k == cedula:
                cuenta1 = 1
                break
        if cuenta1 == 1:
            break
    if cuenta1 == 0:
        archivoreto = open("agenda.txt", "a")
        archivoreto.writelines(nombre + "\n")
        archivoreto.writelines(cedula + "\n")
        archivoreto.writelines(numero + "\n")
        archivoreto.close()
def buscarbene(li,buscar):
    donde=[]
    for i in li:
        for k in i:
            if k == buscar:
                donde=i
    return donde
def borrarbene(aaa,cel):
    for i in aaa:
        for k in i:
            if k == cel:
                aaa.remove(i)
    archivoreto = open("agenda.txt", "w")
    for i in aaa:
        for k in i:
            archivoreto.write(str(k) + "\n")
    archivoreto.close()
cuenta = 0
while True:
    print("Menu Principal")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    print("6. Salir")
    entrada = int(input())
    if entrada == 1:
        print("Listado de beneficiarios")
        datoss = datosenlista()
        for i in datoss:
            for k in i:
                print(k)
        continue
    elif entrada == 2:
        print("Digite la letra por la que empiezan los beneficiarios:")
        letra = input()
        print("Listado filtrado de beneficiarios:")
        nueva = datosenlista()
        resultados = []
        for i in nueva:
            for k in i:
                if k[0].startswith(letra):
                    resultados += i
        for g in resultados:
            print(g)
        continue
    elif entrada == 3:
        print("Digite la información del beneficiario a agregar:")
        nombre = input()
        cedula = input()
        numero = input()
        archivoreto = open("agenda.txt", "r")
        lineas = archivoreto.readlines()
        archivoreto.close()
        tamanoline = (len(lineas))
        if tamanoline==0:
            agregar1(nombre, cedula, numero)
        else:
            agregar12(nombre, cedula, numero, datosenlista())
        print("El beneficiario ha sido agregado")
        continue
    elif entrada == 4:
        print("Digite el nombre y apellido del beneficiario a buscar:")
        buscar = input()
        li=datosenlista()
        filtro=buscarbene(li,buscar)
        print(filtro[0])
        print(filtro[1])
        print(filtro[2])
        continue
    elif entrada == 5:
        print("Digite la cedula del beneficiario a borrar:")
        aaa = datosenlista()
        cel = input()
        borrarbene(aaa,cel)
        print("El usuario ha sido eliminado del listado")
        continue
    elif entrada == 6:
        print("Hasta pronto")
        break