terminar=True
cuenta_dias=0
dias_maximas=0
dias_minimos=0
dias_ambos=0
cuenta_promedio=0
promedio_max=0
promedio_min=0
media_tempmax=0
media_tempmin=0

while terminar:
    Temperatura_Max=int(input())
    Temperatura_Min=int(input())

    if Temperatura_Max==0 and Temperatura_Min==0:
        terminar=False
    elif Temperatura_Max > 35 and Temperatura_Min < 5:
        dias_ambos += 1
        cuenta_dias += 1
    elif Temperatura_Max>35:
        dias_maximas+=1
        cuenta_dias += 1
    elif Temperatura_Min<5:
        dias_minimos+=1
        cuenta_dias += 1
    else:
        cuenta_dias+=1
        cuenta_promedio+=1

        promedio_max=promedio_max+Temperatura_Max
        promedio_min=promedio_min+Temperatura_Min
        media_tempmax=promedio_max/cuenta_promedio
        media_tempmin=promedio_min/cuenta_promedio
Dias_error = dias_minimos + dias_maximas + dias_ambos
porcentaje_dias_error=(Dias_error/cuenta_dias)*100


print(cuenta_dias)
print(Dias_error)
print(dias_minimos)
print(dias_maximas)
print(dias_ambos)
print(media_tempmax)
print(media_tempmin)
print(porcentaje_dias_error)

