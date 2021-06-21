def isPrime(num):
    for i in range(2,num):

        if i==0 or i==1:
            continue
        if num % (i) == 0:
            return False
    return True

 ####este codigo saca los numero primos






for i in range(1, 20):
    if isPrime(i + 1)==True:
        print(i+1, end=" ")
print()