
import time

print('realizar un pollo a la moostaza')
time.sleep(2)
print('ingredientes: pechuga, sal, crema de leche, miel, mostaza')
time.sleep(2)
comprar=True
while comprar:
    print('¿tenemos todos los ingredientes en casa?')
    ingre = input()
    if ingre.__contains__("no"):
        print('comprar los ingredientes que te hacen falta')
    else:
        comprar=False
time.sleep(2)
print('lavar muy bien los ingredientes')
time.sleep(2)
print('agregar sal a los cubos de pechuga')
time.sleep(2)
print('cortar la pechuga en cubos pequeños')
time.sleep(2)
print('calentar el sarten')
time.sleep(2)

cal=True
while cal:
    print('¿esta caliente el sarten?')
    sarten = input()
    if sarten.__contains__("no"):
        print('calentar por 3 minutos')
    else:
        cal=False
print('agregar aceite')
time.sleep(2)
print('asar los trozos de pechuga por ambos lados')
time.sleep(2)
print('mezclar la salsa: 3 cucharadas de crema de leche, 3 cucharadas de miel')
time.sleep(2)
print('una cucharada de mostaza y una pizca de sal')
time.sleep(2)
print('poner los trozos de pechuga en la mezcla anterior')
time.sleep(2)
print('poner otra sarten y poner los trozos de pechuga bañados en la salsa')
time.sleep(2)
dorado=True
while dorado:
    print('ya estan dorados')
    estandorados=input()
    if estandorados.__contains__('no'):
        continue
    else:
        dorado=False

print('servir y dusfrutar')






