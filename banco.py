x,y=(input()).split()
x=float(x)
y=float(y)
if x%5==0:
    x=x+0.50
    if x<=y:
        y=y-x
        y="{:.2f}".format(y)
        print(y)
    else:
        y = "{:.2f}".format(y)
        print(y)
else:
    y = "{:.2f}".format(y)
    print(y)

