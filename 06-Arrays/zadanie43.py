def matrix(n):
    arr = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if j == i:
                arr[i][j] = 1

    return arr

def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


printArr(matrix(3))
printArr(matrix(5))
printArr(matrix(8))