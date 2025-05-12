t=0
w=str(input())

for i in range(len(w)):
    if w[i] in ['A', 'B', 'C']:
        t+=3
    elif w[i]in ['D' , 'E' , 'F']:
        t+=4
    elif w[i]in ['G', 'H', 'I']:
        t+=5
    elif w[i]in ['J' , 'K' , 'L']:
        t+=6
    elif w[i]in ['M' , 'N' , 'O']:
        t+=7
    elif w[i] in ['P','Q' , 'R' , 'S']:
        t+=8
    elif w[i] in ['T' ,'U', 'V']:
        t+=9
    else:
        t+=10

print(t)