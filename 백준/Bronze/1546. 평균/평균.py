n=int(input())
a=list(map(int,input().split()))
a.sort()
m=0
for i in range(n):
    k=a[i]/a[n-1]*100 
    m+=k
print(m/n)