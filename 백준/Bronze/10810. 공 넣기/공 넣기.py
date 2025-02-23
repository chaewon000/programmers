n,m=map(int,input().split())
N={}
for i in range (n):
    N[i+1]=0
for i in range(m):
    i,j,k=map(int,input().split())
    for i in range (i,j+1):
        N[i]=k
print(' '.join(map(str,N.values())))