n=int(input())
x=list(map(int,input().split()))
x.sort()
print(x[0],x[n-1])