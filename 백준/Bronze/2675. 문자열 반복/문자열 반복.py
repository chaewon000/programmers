t=int(input())
for i in range (t):
    r,s=(input().split())
    r=int(r)
    R=''
    for i in range(len(s)):
        R+=s[i]*r
    print(R)