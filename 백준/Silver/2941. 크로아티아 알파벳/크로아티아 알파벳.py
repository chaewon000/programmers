cro_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
text = input()

for cro in cro_list:
    text = text.replace(cro, '*')  
print(len(text))