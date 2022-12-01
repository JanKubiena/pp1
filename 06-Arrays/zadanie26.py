arr = [5,1,9,6,1]
arr2 = []
secondMax = 0

arr.sort()

for i in arr: 
    if i not in arr2:
        arr2.append(i)

secondMax = arr2[-2]

print(secondMax)