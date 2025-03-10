a,b=(input().split())

a=list(a)
b=list(b)

a.reverse()
b.reverse()

a=a[0]+a[1]+a[2]
b= b[0]+b[1]+b[2]

k=[]
k.append(a)
k.append(b)

k.sort()
print(k[1])