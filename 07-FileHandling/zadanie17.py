file = open("lorem.txt", "r", encoding="utf-8")
copiedFile = open("copiedLibeByLine.txt", "w", encoding="utf-8")

for i in file:
    copiedFile.write(i)

file.close()
copiedFile.close()