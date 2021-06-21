miDirectorioTelefonico = {}    # un diccionario vacio

miDirectorioTelefonico ["Adan"] = ["3456783958", "098098"]
miDirectorioTelefonico ["camilo"] = ["123423asdf", "asdfasdf"]# crear o añadir un par clave-valor
print(miDirectorioTelefonico)    # salida: {'Adan': 3456783958}

del miDirectorioTelefonico ["Adan"]
print(miDirectorioTelefonico)    # salida: {}