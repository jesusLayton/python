def horasnormales (horas,valor):
    salario_normal = horas*valor
    return salario_normal
def extra(horas,valor):
    extras=(horas-40)*1.5*valor
    return extras
def descuentospara(parafiscales):
    total_para=parafiscales*0.09
    return total_para
def total_pri(prima):
    total_prima=prima*0.0833
    return total_prima
def cesan(cesantias):
    total_cesa=cesantias*0.0833
    return total_cesa
def interes_cesa(intcesa):
    total_intcesa=intcesa*0.01
    return  total_intcesa
def vacascio(vacas):
    vacaciones=vacas*0.0417
    return vacaciones
def des_salud(salud):
    tota_salud=salud*0.04
    return tota_salud
def despen(pension):
    tota_pension=pension*0.04
    return tota_pension

horas=int(input())
valor_hora=int(input())

if horas<=40:
    salarionormal=horasnormales(horas,valor_hora)
    sal_extra=0
else:
    salarionormal=valor_hora*40
    sal_extra=extra(horas,valor_hora)


salario_bruto=salarionormal+sal_extra
total_para=descuentospara(salario_bruto)
tota_salud=des_salud(salario_bruto)
tota_pension=despen(salario_bruto)
descuentos=total_para+tota_salud+tota_pension

total_prima=total_pri(salario_bruto)
total_cesa=cesan(salario_bruto)
total_intsesa=interes_cesa(salario_bruto)
vacaciones=vacascio(salario_bruto)

print(salarionormal)
print(sal_extra)
print(salario_bruto)
print(total_para)
print(tota_salud)
print(tota_pension)
print(descuentos)
print(salario_bruto-descuentos)
print(total_prima)
print(total_cesa)
print(total_intsesa)
print(vacaciones)






