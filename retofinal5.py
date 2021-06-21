def datosenlista():
    archivoreto = open("agenda.txt", "r")
    lineas = archivoreto.readlines()
    listaordenada = []
    salida = []
    for linea in lineas:
        salida.append(linea.replace("\n", ""))
        listaordenada = [salida[i:i + 3] for i in range(0, len(salida), 3)]
    return listaordenada





archivoreto = open("agenda.txt")
archivoreto.close()



while True:
    print("menu princial")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario ")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    print("6. Salir)")
    entrada = int(input())
    if entrada==1:
        datoss=datosenlista()
        for i  in datoss:
            for k in i:
                print(k)
        continue


    elif entrada==2:

        letra=input()
        nueva=datosenlista()
        resultados = []
        for i in nueva:
            for k in i:
                if k[0].lower().startswith(letra):
                    resultados+=i

        for g in resultados:
            print(g)

        continue



    elif entrada == 3:
        orden=datosenlista()
        # despues de que tenga la lista ordenada, se realiza la comparacion de las cedula
        # si estan repetidas, no se puede escribir el nuevo usiario

        print("ingrese un nuevo usuario")

        cuenta = 0
        archivoreto = open("agenda.txt", "a")
        while True:
            nombre = input().lower()
            cedula = input()
            numero = input()
            for i in datosenlista():
                for k in i:

                    if k == cedula:
                        cuenta = 1
                        break

                if cuenta == 1:
                    break

            if cuenta == 1:
                continue
            else:
                break

        archivoreto.writelines(nombre + "\n")
        archivoreto.writelines(cedula + "\n")
        archivoreto.writelines(numero + "\n")
        print("usuario ingresado con exito")
        archivoreto.close()

    elif entrada == 4:
        buscar=input().lower()
        #buscar usuario con su nombre
        for i in datosenlista() :
            for k in i:
                if k==buscar:
                    print(i[1])
                    print(i[2])
        archivoreto.close()

    elif entrada == 5:

        aaa=datosenlista()

        cel = input()

        for i in aaa:
            for k in i:
                if k==cel:
                    aaa.remove(i)


        archivoreto=open("agenda.txt","w")

        for i in aaa:
            for k in i:
                archivoreto.write(str(k)+"\n")
        archivoreto.close()

    elif entrada == 6:

        break

    else:

        continue





