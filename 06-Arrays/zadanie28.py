def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def medianOfArray(arr):
    median = 0
    if len(arr) % 2 == 1:
        median = arr[int(len(arr) / 2)]
    else:
        median = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1]) / 2

    return median

print(medianOfArray(bubbleSort([1,0,9,4,6,8])))



