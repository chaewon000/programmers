n,m=map(int,input().split())
lst_a =[[int(x) for x in input().split()] for _ in range(n)]

lst_b =[[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    n=i
    lst_sum=[]
    for k in range(m):
        lst_sum.append(lst_a[n][k]+lst_b[n][k])
    print(' '.join(map(str,lst_sum)))