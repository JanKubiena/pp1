def arrToString(arr):
    string = ""
    for i in arr:
        string += str(i) + ", "
        
    string = string[:-2]
    return string

print(arrToString([1,2,3,4,5]))