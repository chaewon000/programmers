a, b, c=map(int,input().split())
if a==b==c:
    price=10000+a*1000
elif a==b or a==c:
    price=1000+a*100
elif b==c:
    price=1000+b*100
else: 
    if a>b and a>c:
        price=a*100
    elif b>a and b>c:
        price=b*100
    else:
        price=c*100
print(price)
    