arr = [2,3,2,5,8,1,9,8]
arr2 = []

for i in range(len(arr)):
    flag = True
    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            flag = False
            break
    if flag:
        arr2.append(arr[i])

print(arr2)
