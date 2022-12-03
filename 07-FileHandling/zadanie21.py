import math

file = open("powers.txt", "w", encoding="utf-8")
i = 1
while i < 11:
    for j in range(1, 4):
        power = int(math.pow(i, j))
        file.write(str(power))
        if j != 3:
            file.write(", ")
    file.write("\n")

    i+=1

file.close()