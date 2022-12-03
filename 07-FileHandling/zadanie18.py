file = open("meat.txt", "r", encoding="utf-8")
file2 = open("bread.txt", "r", encoding="utf-8")
shoppingList = open("shoppingList.txt", "w", encoding="utf-8")

def writeToShoppingList(file):
    for i in file:
        shoppingList.write(i)

writeToShoppingList(file)
writeToShoppingList(file2)

file.close()
file2.close()
shoppingList.close()