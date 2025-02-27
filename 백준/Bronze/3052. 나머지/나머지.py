#4-8
a=[]
for i in range(10):
    k=int(input())
    a.append(k)
b=[]
for i in range(10):
    k=a[i]%42
    b.append(k)
print(len(list(set(b))))