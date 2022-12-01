def smallerThan(n, arr):
    numberOfGrater = 0
    for i in arr:
        if i > n:
            numberOfGrater += 1
        
    return numberOfGrater

print(smallerThan(2, [1,2,3,4,5]))