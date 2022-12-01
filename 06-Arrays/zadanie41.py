arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
print()
for i in range(len(arr[0])):
    arr[0][i], arr[-1][i] = arr[-1][i], arr[0][i]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
