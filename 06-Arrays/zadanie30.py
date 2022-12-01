def minmax(arr):
    newArr = []
    newArr.append(min(arr))
    newArr.append(max(arr))

    return newArr 

print(minmax([4,2,8,4,7,9,5]))
