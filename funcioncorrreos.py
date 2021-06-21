import requests
def verificarcorreo(correo):
    r=requests.get("https://api.eva.pingutil.com/email?email="+correo)
    info=r.json()
    salida=""
    for data in info:
        salida+=str(data)+": "+str(info[data])+"\n"
    return salida

print(verificarcorreo("roca230313@gmail.com"))