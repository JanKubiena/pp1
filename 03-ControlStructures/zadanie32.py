arr = [[0 for i in range(7)] for j in range(7)]

for i in range(7):
    help = i + 1
    for j in range(7):
        arr[i][j] = help
        help = help + 7

for i in range(7):
    for j in range(7):
        print(arr[i][j], end=" ")
    print()