import sys

while True:
    try:
        line=sys.stdin.readline().rstrip()
        a,b=map(int,line.split())
        print(a+b)
    except:
        break
