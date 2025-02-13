import sys
t=int(input())
x=1
while x<=t:
    a,b=sys.stdin.readline().rstrip().split()
    a=int(float(a))
    b=int(float(b))
    print(f'Case #{x}:',a+b)
    x+=1
    