H,M=map(int,input().split())
if H==0:
    if M>=45:
        M-=45
    else:
        H+=24
        H-=1
        M+=60
        M-=45
else:
    if M>=45:
        M-=45
    else:
        H-=1
        M+=60
        M-=45
print(H,M)
