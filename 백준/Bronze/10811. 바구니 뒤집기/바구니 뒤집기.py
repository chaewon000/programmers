a=[]
n,m=map(int,input().split())
for i in range(n):
    a.append(i+1)
for x in range(m):
    i,j=map(int,input().split())
    b=a[i-1:j]
    b.reverse()
    for x in range(j-i+1):
        k=b[x]
        a[i-1+x]=k
print(' '.join(map(str,a)))