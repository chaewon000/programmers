import sys
t=int(input())
for x in range(t):
    a,b=sys.stdin.readline().rstrip().split()
    a=int(float(a))
    b=int(float(b))
    print(f'Case #{x+1}: {a} + {b} =',a+b)
    