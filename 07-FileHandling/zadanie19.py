file = open("numbers_1-50.txt", "w", encoding="utf-8")
i = 1
while i < 51:
    file.write(str(i))
    file.write("\n")
    i+=1

file.close()