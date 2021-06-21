# musicos=[
#     "guitarra",
#     "bongoes",
#     "tipes",
#     "liras",
#     "tipes",
#     "tipes",
#     "timbales",
#     "michrofonos",
#     "atril"
# ]
#
# num=[
#     "1",
#     "56",
#     "456",
#     "65",
#     "65"
# ]
#
# def agregarjuego(nuevojuego):
#     global musicos
#     musicos.append(nuevojuego)
#
#
# def agregarjuegoposicion(pos,nuevojuego):
#     global musicos
#     musicos.insert(pos, nuevojuego)
#
#
#
# def modificarjuego(pos,actualizarjuego):
#     global musicos
#     musicos[pos]=actualizarjuego
#
#
# def eliminardato(datoeliminar):
#     global musicos
#     musicos.remove(datoeliminar)
#
#
# def eliminardatoposicion(pos):
#     global musicos
#     del musicos[pos]
#
#
# def ordenarjuegos():
#     global musicos
#     musicos.sort()
#
# def ordenanum():
#     global num
#     num.sort()
#
# #
# # print(musicos)
# # print(ordenarjuegos())
# # print(musicos)
# # print(num)
# # print(ordenanum())
# # print(num)
#
#
# def contarjuego(juegoacontar):
#     global musicos
#     resultado=musicos.count(juegoacontar)
#     return resultado
#
#
#
# # print(musicos)
# # print(contarjuego("tipes"))
# # print(musicos)
# # print(num)
# # print(ordenanum())
# # print(num)
#
# def limpiarjuegos():
#     global musicos
#     musicos.clear()
#
# print(musicos)
# print(limpiarjuegos())
# print(musicos)
#
#
#
#
# listanumeros=[[y for y in range(10)] for x in range(10)]
# for filas in range(10):
#     for columnas in range(10):
#         print(listanumeros[filas][columnas], end=" ")
#     print()

# comidas=[
#     "pizza",
#     "lasagna"
#     "tofu",
#     "ajiaco",
#     "perro caliente",
#     "hamburguesa",
#     "arroz con pollo",
#     "sushi"
# ]
#
# nombres=(
#     "jesus",
#     "jorge",
#     "gloria",
#     "paula",
#     "carolina",
#     "luis",
#     "jeniffer",
#     "alexander",
#     "steven",
#     "diana",
#     "daniel",
#     "bryam",
#     "carlos",
#     "alfonso",
#     "pablo"
# )
#
# # print("luis" in nombres)
# # print(nombres.__contains__("LUIS"))
# # print(nombres[4])
#
# nuevalista=list(nombres)
# nuevatupla=tuple(comidas)
# print(comidas)
# print(nuevatupla)
# print(nombres)
# print(nuevalista)

# pizzaconpina={
#     "alfonso",
#     "oscar",
#     "jesus",
#     "alexander",
#     "daniela",
#     "jorge",
#     "daniel",
#     "karen"
# }
# pizzasinpina={
#     "stiven",
#     "jaidith",
#     "andres",
#     "stephany",
#     "paula",
#     "carolina",
#     "paola",
#     "maoly",
#     "diego"
# }
#
#
# # print(pizzaconpina.union(pizzasinpina))
#
# hamburguesa={
#     "jeniffer",
#     "jonathan",
#     "jesus",
#     "jorge",
#     "diego",
#     "jorge h",
#     "paula",
#     "pablo",
#     "jaidith",
#     "ivonne"
# }
# perrocaliente={
#     "jesus",
#     "jonathan",
#     "diana",
#     "jorge",
#     "daniel",
#     "pablo",
#     "alexander",
#     "ivonne",
#     "nidia",
#     "bryam",
#     "stephany",
#     "ivonne m"
# }
# print(hamburguesa.difference(perrocaliente))

# colorfavorito=[
#     ("daniela","amarillo"),
#     ("alexander","azul"),
#     ("ivonne n","fucsia","rosado"),
#     ("karen","blanco"),
#     ("carlos","verde"),
#     ("steven","negro"),
#     ("juan","azul"),
#     ("marcela","salmon"),
#     "hola"
# ]
# print(type(colorfavorito[2]))
#
# for fila in range(len(colorfavorito)):
#     for columna in range(len(colorfavorito[fila])):
#         print(colorfavorito[fila][columna],end=" ")
#     print()
#
# lista=[x for x in range(10,0,-1)]
# tupla=(x for x in range(10))
# set={x for x in range(10)}
# print(*lista)
# print(*tupla)
# print(*set)

pizzaconpina={
    "alfonso",
    "oscar",
    "jesus",
    "alexander",
    "daniela",
    "jorge",
    "daniel",
    "karen"
}
pizzasinpina={
    "stiven",
    "jaidith",
    "andres",
    "stephany",
    "paula",
    "carolina",
    "paola",
    "maoly",
    "diego"
}

# print(pizzaconpina.union(pizzasinpina))

hamburguesa={
    "jeniffer",
    "jonathan",
    "jesus",
    "jorge",
    "diego",
    "jorge h",
    "paula",
    "pablo",
    "jaidith",
    "ivonne"
}
perrocaliente={
    "jesus",
    "jonathan",
    "diana",
    "jorge",
    "daniel",
    "pablo",
    "alexander",
    "ivonne",
    "nidia",
    "bryam",
    "stephany",
    "ivonne m"
}

paisesamerica={
    "polombia",
    "chile",
    "panama",
    "argentina",
    "venezuela",
    "brazil",
    "ecuador",
    "canada"
}

paisesasiaticos={
    "japon",
    "filipinas",
    "tailandia",
    "rusia",
    "mongolia",
    "china",
    "surcorea",
    "pakistan"
}

paisesoceania={
    "australia",
    "nueva zelanda",
    "fiji",
    "samoa"
}

paisesdelmundo={
    "australia",
    "nueva zelanda",
    "fiji",
    "samoa",
    "japon",
    "filipinas",
    "tailandia",
    "rusia",
    "mongolia",
    "china",
    "surcorea",
    "pakistan",
    "polombia",
    "chile",
    "panama",
    "argentina",
    "venezuela",
    "brazil",
    "ecuador",
    "canada"
}


print(paisesdelmundo.issuperset(paisesoceania))
print(paisesamerica.issubset(paisesdelmundo))



print(hamburguesa.difference(perrocaliente))
lista=list(hamburguesa)
tupla=tuple(hamburguesa)
set=set(hamburguesa)