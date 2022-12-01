arr = [[0 for i in range(5)] for j in range(5)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (i+1)*(j+1)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()