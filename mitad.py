t=int(input())
for i in range(t):
    A,B,C=input().split()
    A=int(A)
    B=int(B)
    C=int(C)
    if ((A < B < C) or (A > B > C)):
        print(B)
    elif ((B < A < C) or (B > A > C)):
        print(A)
    else:
        print(C)
