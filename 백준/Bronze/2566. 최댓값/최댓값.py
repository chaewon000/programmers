maxs={}
for i in range(9):
    lst = [int(x) for x in input().split()]
    maxslst=[i+1,lst.index(max(lst))+1]
    maxs [max(lst)] = [maxslst]


max_num=maxs[max(maxs.keys())][0]
print(max(maxs.keys()))
print(' '.join(map(str,max_num)))