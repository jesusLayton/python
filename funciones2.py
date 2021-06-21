lista = [1,2,3,4,5,6,7,8,9,0]
cadena="holamundosoyunacadenasaludenme"
palabras=["hola","mundo","soy","lista"]

def imprimirconjunto(conjunto):
    for dato in conjunto:
        if dato==conjunto[len(conjunto)-1]:
            print(dato, end="")
            break
        print(dato, end="->")
    print()


imprimirconjunto(lista)
imprimirconjunto(cadena)
imprimirconjunto(palabras)
