n=int(input())
num=0
for i in range(n):
    text=input()
    text2=text
    for i in range(len(text)):
        text2=text2.replace(text[i],'*')

        text2=text2.lstrip('*')

        if '*' in text2:
            break 
    if '*' in text2:
        num+=0
    else:
        num+=1

print(num)