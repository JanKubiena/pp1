arr = [1,2,3,4,5]

#a
arr[0] -= 1
#b
arr[-1] += 4
#c
arr[len(arr)//2] *= 2
#d
for i in range(len(arr)):
    arr[i] += 3

print(arr)
