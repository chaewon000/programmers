string = []
for i in range(5):
    string.append(input())  

final = ""
max_length = max(len(s) for s in string)  

for i in range(max_length):
    for x in range(5):
        if i < len(string[x]):
            final += string[x][i]  

print(final)