def separateEvenAndOdd(arr):

    counter = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[counter] = arr[counter], arr[i]
            counter += 1
            
    
    return arr

arr = [1,2,6,4,5,3,7,8]
separateEvenAndOdd(arr)
print(arr)
