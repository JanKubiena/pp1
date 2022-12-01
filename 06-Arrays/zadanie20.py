def star(n):
    stars = ""
    for i in range(n):
        stars += "*"

    return stars

arr = [12,6,4,9,10]

for i in range(len(arr)):
    print(arr[i], ": ", star(arr[i]))