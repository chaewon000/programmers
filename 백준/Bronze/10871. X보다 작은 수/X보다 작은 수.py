a,b=map(int,input().split())
y=list(map(int,input().split()))
k=(list(filter(lambda x: x < b, y)))
print(' '.join(map(str,k)))