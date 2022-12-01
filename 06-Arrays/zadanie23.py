def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr
 
arr = [8,3,2,5,7,1]

print(bubbleSort(arr))