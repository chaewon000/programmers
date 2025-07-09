for i in range(3):
    n=int(input())
    k=0
    for i in range(n):
        k+=int(input())
    if k==0:
        print(0)
    elif k<0:
        print('-')
    else:
        print('+')