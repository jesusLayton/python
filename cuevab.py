t=int(input())
num=[]
for i in range(t):
    list=int(input())
    num.append(list)

lista=num

for i in range(1, len(lista)):
    actual=lista[i]
    indice=i

    while indice>0 and lista[indice -1]>actual:
        lista[indice]=lista[indice-1]
        indice=indice-1
    lista[indice]=actual

print(lista)
