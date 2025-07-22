a,b,c=map(int,input().split())
lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
lst.sort()
print(' '.join(map(str,lst)))