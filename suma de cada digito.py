t=int(input())
for i in range(t):
    n=input()
    tm=len(n)
    resul1=0
    for j in range(tm):
        salida=n[j]
        resul=int(salida)
        resul1=resul1+resul
    print(resul1)
