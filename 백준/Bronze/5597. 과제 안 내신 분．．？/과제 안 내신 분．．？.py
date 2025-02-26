a=[]
for i in range(1,31):
    a.append(i)
b=[]
for i in range(28):
    k=int(input())
    b.append(k)
a=set(a)
b=set(b)
c=(list(a-b))
c.sort()
print(c[0])
print(c[1])