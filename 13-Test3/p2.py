def f(arr):  
    tempArr  = [[0 for i in range(len(arr))] for j in range(len(arr[0]))]
    for i in range(len(arr) - 1):
        for j in range(len(arr[i])):
            tempArr[i][j] = arr[i][j] * (i+2)
            if tempArr[i][j] == arr[i+1][j]:
                continue
            else:
                return False

    return True



print(f([[1,2,3],[2,4,6]]))


