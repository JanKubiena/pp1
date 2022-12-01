arr = [[i for i in range(4)] for j in range(2)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()