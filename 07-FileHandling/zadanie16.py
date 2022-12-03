file = open("lorem.txt", "r", encoding="utf-8")
file_content = file.read()
copiedFile = open("copiedWhole.txt", "w", encoding="utf-8")

copiedFile.write(file_content)

file.close()
copiedFile.close()

