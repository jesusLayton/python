nombre=input("Por favor ingrese su nombre: ")
edad1=True
while edad1:
    edad=int(input("Ingrese su edad: "))
    if edad>=15:
        break
ingreso=float(input("Ingrese el saliario minimo en decimal de familia: "))
puntaje=int(input("Por favor ingrese el puntaje obtenido (valor entre 0 y 100): "))



if edad>=15 and edad<=18:
    por_edad=25
elif edad>=19 and edad<=21:
    por_edad=15
elif edad>=22 and edad<=25:
    por_edad=10
else:
    por_edad=0

if ingreso<=1:
    por_ing=30
elif ingreso>1 and ingreso<=2:
    por_ing=20
elif ingreso>2 and ingreso<=3:
    por_ing=10
elif ingreso>3 and ingreso<=4:
    por_ing = 5
else:
    por_ing=0

if puntaje>=80 and puntaje<86:
    por_pun=30
elif puntaje>=86 and puntaje<91:
    por_pun=35
elif puntaje>=91 and puntaje<96:
    por_pun=40
elif puntaje>=96:
    por_pun=45
else:
    por_pun=0

por_total=por_pun+por_ing+por_edad
print(nombre)
print("el valor total de descuento en porcentaje es: ", por_total,"%")
print("el descueto por edad es: ",por_edad,"%")
print("el descuento por salario es: ", por_ing,"%")
print("el descuento por puntaje es: ", por_pun,'%')





