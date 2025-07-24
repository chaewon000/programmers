import sys

k, n, m = map(int, sys.stdin.readline().split())
result = k*n-m

if result < 0:
    result=0

print(result)