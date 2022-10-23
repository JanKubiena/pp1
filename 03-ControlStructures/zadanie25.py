#columns
a  = 15
#rows 
b = 4
rectangleShapeArr = [[0 for i in range(a)] for j in range(b)]

for i in range(b):
    for j in range(a):
        if i == 0 or i == b - 1:
            rectangleShapeArr[i][j] = "*"
        elif j == 0 or j == a - 1:
             rectangleShapeArr[i][j] = "*"
        else:
            rectangleShapeArr[i][j] = " "

# for i in rectangleShapeArr:
#     for j in i:
#         print(j, end='')
#     print()

for i in range(b):
    for j in range(a):
        print(rectangleShapeArr[i][j], end="")
    print()

