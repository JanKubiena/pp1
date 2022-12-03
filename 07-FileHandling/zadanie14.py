whichFile = input("podaj plik: ")
f = open(whichFile, "r", encoding="utf-8")
count = 0
for i in f:
    count += 1

f.close()
print(count)

