import sys

n=int(input())
i=1
while i <= n:
    i+=1
    a,b=sys.stdin.readline().rstrip().split()
    c=int(float(a))
    d=int(float(b))
    print(c+d)