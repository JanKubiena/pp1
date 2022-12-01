def transpose_matrix(arr):
    ready = [[0 for i in range(len(arr))] for j in range(len(arr[0]))]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ready[j][i] = arr[i][j]

    return ready

def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()

TwoDArr = [[1,2,3],[4,5,6]]
print(TwoDArr)

printArr(transpose_matrix(TwoDArr))

    
