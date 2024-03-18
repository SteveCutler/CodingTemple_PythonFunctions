# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
grades = [75, 62, 90, 92, 87, 76, 70, 97, 90, 33]

def averageGrades(*classGrades):
    total = 0
    gradeCount = len(classGrades)
    for x in classGrades:
        total+=x

    average = total/gradeCount
    return average

gradeAverage = averageGrades(*grades)
print(f"the average grade is: {gradeAverage}")
# Task 2: Implement a function to find the highest and lowest grade.

def highLow(classGrades):
    highGrade = max(classGrades)
    lowGrade = min(classGrades)
   
    return highGrade, lowGrade

highGrade, lowGrade = highLow(grades)
print(f"the highest grade is: {highGrade}, the lowest grade is: {lowGrade}")


# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
Alist =[]
Blist =[]
Clist =[]
Dlist =[]
Elist =[]

for x in grades:
    if x >= 90:
        Alist.append(x)
    elif x >= 80:
        Blist.append(x)
    elif x >= 70:
        Clist.append(x)
    elif x >= 60:
        Dlist.append(x)
    else:
        Elist.append(x)

print(f"A grades:{Alist}, B grades: {Blist}, C grades: {Clist}, D grades: {Dlist}, E grades: {Elist}")
        