matriz = []

fil = int(input())
col = int(input())


for i in range(fil):
    matriz.append([0]*col)

for f in range(fil):
    for c range(col):
        matriz[f][c]=int(input(% (f,c)))

print matriz