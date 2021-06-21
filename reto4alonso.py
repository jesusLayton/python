def Valor_horas_normales(ht,vh):
    resultado=ht*vh
    return resultado

def Valor_horas_extras(he,vh):
    resultado1 = he * 1.5 * vh
    return resultado1

def Descuento_parafiscales(x1):
    return x1*0.09

def Descuento_salud(x2):
    return x2*0.04

def Descuento_pension(x3):
    return x3*0.04

def Descuento_prima(x3):
    return x3*0.0833

def Descuento_cesantias(x3):
    return x3*0.0833

def Descuento_int_cesantias(x3):
    return x3*0.01

def Descuento_vacaciones(x3):
    return x3*0.0417


ht=int(input())
vh=int(input())


if ht<=40:
    he=0

else:
    he=ht-40
    ht = 40

Sueldo_bruto=Valor_horas_normales(ht,vh)+Valor_horas_extras(he,vh)
Salida_parafiscales=Descuento_parafiscales(Sueldo_bruto)
Salida_salud=Descuento_salud(Sueldo_bruto)
Salida_pension=Descuento_pension(Sueldo_bruto)
Descuentos_total=Salida_parafiscales+Salida_salud+Salida_pension

Sueldo_neto=Sueldo_bruto-Descuentos_total

Salida_prima=Descuento_prima(Sueldo_bruto)
Salida_cesantias=Descuento_cesantias(Sueldo_bruto)
Salida_int_cesantias=Descuento_int_cesantias(Sueldo_bruto)
Salida_vacaciones=Descuento_vacaciones(Sueldo_bruto)



print(Valor_horas_normales(ht,vh))
print(Valor_horas_extras(he,vh))
print(Sueldo_bruto)
print(Salida_parafiscales)
print(Salida_salud)
print(Salida_pension)
print(Descuentos_total)
print(Sueldo_neto)
print(Salida_prima)
print(Salida_cesantias)
print(Salida_int_cesantias)
print(Salida_vacaciones)