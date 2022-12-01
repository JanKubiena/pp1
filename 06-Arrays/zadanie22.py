arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
arr3 = []

for i in range(len(arr1)):
    flag = True
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            flag = False
            break
    if flag:
        arr3.append(arr1[i])

print(arr3)