a={}
for i in range(1,10):
    t=int(input())
    a[t]=i

v=list(a.keys())
v.sort()
k=v[8]
print(k)
print(a.get(k))