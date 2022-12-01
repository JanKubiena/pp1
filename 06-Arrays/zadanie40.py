def minInArr(arr):

    min = arr[0][0]
    index1 = 0
    index2 = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min:
                min = arr[i][j]
                index1 = i
                index2 = j

    return min, index1, index2

def maxInArr(arr):

    max = 0
    index1 = 0
    index2 = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max:
                max = arr[i][j]
                index1 = i
                index2 = j

    return max, index1, index2


arr = [[38,19], [5,40], [-7,11], [29,16]]

print(minInArr(arr))
print(maxInArr(arr))

