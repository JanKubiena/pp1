import re

file = open('grades.txt','r', encoding="utf-8")

for line in file:
    sum = 0
    avg = 0
    grades = re.findall("[0123456789]..", line)
    if len(grades) > 0:
        for j in grades:
            sum += float(j)
        avg = sum / len(grades)
        print(name, ": ", avg)
    else:
        nameLine = line.split()
        if len(nameLine) > 0:
            name = nameLine[1]

file.close()






