s=input()
a=[]
for i in range(97,123):  #a-z
        
        b=s.find(chr(i))
        a.append(b)

print(' '.join(map(str,a)))