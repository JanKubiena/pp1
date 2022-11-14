arr = ["Genowefa", "Onfury", "Celestyna", "Alojzy", "Pankracy"]

max = 0
index = 0

for i in range(len(arr)):
    if len(arr[i]) > max:
        max = len(arr[i])
        index = i

print(arr[index])