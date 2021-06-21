x,y=input().split()
x=float(x)
y=float(y)
if x<y and x%5==0:
    sal=y-x-0.50
    sal=float(sal)
    sal="{:.2f}".fotmat(sal)
    print(sal)
else:
    y = "{:.2f}".format(y)
    print(y)

