bloques = int(input("Ingrese el número de bloques: "))
altura=0
cuenta=0
terminar=True
while terminar:
    for i in range(bloques):
        altura+=i
        cuenta+=1
        if altura==bloques:
            print("La altura de la pirámide:", cuenta-1)
            terminar=False
        # elif altura!=bloques
        #     print("no te alcanzan los bloques para hace")
        #     break
    break
print(altura)
print(cuenta)