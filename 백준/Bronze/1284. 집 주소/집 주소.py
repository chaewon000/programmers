while True:
    n=input()
    blank=len(n)+1
    for i in range(len(n)):
        if n[i]=='1':
            blank+=2
        elif n[i]=='0':
            blank+=4
        else:
            blank+=3
    if n=='0':
        break
    print(blank)
