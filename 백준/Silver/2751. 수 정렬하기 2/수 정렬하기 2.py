import sys
lst=[]
n=int(input())
lst = [ int(sys.stdin.readline()) for i in range(n) ]

lst.sort()
print( '\n' .join(map(str,lst)))