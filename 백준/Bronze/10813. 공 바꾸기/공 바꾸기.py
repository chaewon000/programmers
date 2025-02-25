#4-5단계 수정
n,m=map(int,input().split())
N={}
for i in range (n):
    N[i+1]=i+1
for i in range(m):
    i,j=map(int,input().split())
    k=list(N.values())
    N[i]=k[j-1]
    N[j]=k[i-1]
print(' '.join(map(str,N.values())))