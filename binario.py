t=input()
t=t[::-1]
cuenta=0
for i in range(len(t)):
    if t[i]=='1':
        salida=2**(i)
        cuenta=cuenta+salida
    else:
        cuenta=cuenta
print(cuenta)

