num_sum=0
grade_sum=0

for i in range (20):
    sub, num, grade=input().split()
    num=float(num)
    if grade[0]=='P' :
        grade_fin=0
        num=0
    else:
        if grade[0]=='A':
            grade_fin=4
        elif grade[0]=='B':
            grade_fin=3
        elif grade[0]=='C':
            grade_fin=2
        elif grade[0]=='D':
            grade_fin=1
        elif grade[0]=='F':
            grade_fin=0
        else :
            grade_fin=0
    if len(grade) > 1 and grade[1]=='+':
        grade_fin+=0.5

    num_sum+=num
    grade_sum+=num*grade_fin
    
print(grade_sum/num_sum)