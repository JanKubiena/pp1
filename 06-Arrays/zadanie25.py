def isInList(n, arr):
    for i in arr:
        if n == i:
            return True

    return False
print(isInList(23, [15, 38, 7, 23, 14]))