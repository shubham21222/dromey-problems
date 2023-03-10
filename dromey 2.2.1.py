marks=[23,50,53,54,62]
list=[]
passing_marks=50
total=0
count=0
for i in range(len(marks)):
    total = sum (marks) 
    print("total sum of all marks: ",total)
    pass_students=marks[i]>=passing_marks
    list.append(pass_students)
    print(list)
    percentage = ((total/500)*100)
    print("total percentage = ", percentage)
