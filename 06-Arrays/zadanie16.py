arr = [15,8,31,47,2,19]
reversedAtrr = [0 for i in range(len(arr))]
a = 0
for i in arr:
    reversedAtrr[len(arr) - 1 - a] = i
    a = a + 1

print(reversedAtrr)