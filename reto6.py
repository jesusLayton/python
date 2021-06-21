from io import open
archivo=open("info.txt","w")

nombre=input()
cedula=input()
celular=input()
archivo.write(nombre)
print()
archivo.write(cedula)
archivo.write(celular)
archivo.closed()