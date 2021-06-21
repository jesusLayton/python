n,k=input().split()
n=int(n)
k=int(k)
salida=0
sal1=0
for i in range(n):
    ti=int(input())
    if ti%k==0:
        salida = salida+1
    elif ti%k != 0:
        sal1=sal1+1
    else:
        salida=salida
print(salida)
print(sal1)