print("He llegado tarde a clase?")
horas=6
minutos=00
while(True):
    print("Por favor inserte la hora en la que llego")
    horallegada,minutollegada=input().split(":")
    horallegada=int(horallegada)
    minutollegada=int(minutollegada)
    if(horallegada>=0 and horallegada<=23 and minutollegada>=0 and minutollegada<=59):
        print("hora valida")
        break
    else:
        print("hora no valida")

if horallegada<=horas:
    if minutollegada==minutos and  horas==horallegada:
        print("llegaste apenas")
    elif minutollegada>minutos and  horas>horallegada:
        print("Llegaste temprano")
    elif horas==horallegada and minutollegada > minutos:
        print("Llegaste :",(minutollegada-minutos), " minutos tarde")
    else:
        print("Llegaste temprano")
else:
    print("Llegaste :", (horallegada - horas), " horas tarde")