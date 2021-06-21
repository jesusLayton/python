#T=int(input())
import f as f

matriz = []

fil = int(input())
#col = int(input())

# se inicia la matriz en ceros
for i in range(fil):
    matriz.append([0]*3)
# ciclo for para llenar la matriz
for f in range(fil):
    for c in range(3):
        matriz[f][c]=int(input((f, c)))

print (matriz)
#tamaño de la matriz
a=len(matriz)
b=len(matriz[0])

print (a,b)

#for j range(fil)
  # for k range(3)
  #      matrizsal =

#A=int(input())
#B=int(input())
#C=int(input())
#if A<B<C or C<B<A:
 #   print(B)
#elif B<A<C or C<A<B:
 #   print(A)
#else:
 #   print(C)
