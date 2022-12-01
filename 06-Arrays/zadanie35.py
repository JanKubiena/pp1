import random

def randElem(arr):
    randomNum = random.choice(arr)

    return randomNum

print(randElem([1,2,3,4,5]))
