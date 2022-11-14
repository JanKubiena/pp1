from ctypes import sizeof


arr = [[2,5,4],[9,0,3]]

print(arr)
print(len(arr), len(arr[0]))
print(arr[0][1])
print(arr[1][2])
for i in range(len(arr[1])):
    print(arr[1][i], end=" ")
print()

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()

for i in range(len(arr)):
    print(arr[i][-1])