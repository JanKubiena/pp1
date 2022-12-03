import random

file = open("randomNumbers.txt", "w", encoding="utf-8")
i = 1
while i < 51:
    randomNum = random.randint(100,1000)
    file.write(str(randomNum))
    file.write("\n")
    i+=1

file.close()