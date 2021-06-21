contadordias = 0
errormax = 0
errormin = 0
diasbien = 0
ambosmal = 0
prommax = 0
prommin = 0
while True:
    tmax = int(input())
    tmin = int(input())
    contadordias += 1
    if tmax == 0 and tmin == 0:
        break
    elif tmax in range(5, 35) and tmin in range(5, 35):  # para suma interna
        diasbien += 1
        prommax += tmax
        prommin += tmin
    elif tmax > 35:
        errormax += 1
    elif tmin < 5:
        errormin += 1

dias = contadordias - 1
diasconerror = dias - diasbien
promediotmax = prommax / diasbien
promediotmin = prommin / diasbien
porcentaje_error = ((diasconerror * 100) / dias)

print(dias)
print(diasconerror)
print(errormin)
print(errormax - 1)
print(promediotmax)
print(promediotmin)
print(porcentaje_error)