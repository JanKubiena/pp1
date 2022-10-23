userAmount = int(input("Podaj całkowita ilość pieniędzy które masz: "))
numberOf5zl = 0
numberOf2zl = 0
numberOf1zl = 0

while(userAmount > 0):
    if userAmount >= 5:
        numberOf5zl += 1
        userAmount -= 5
    elif userAmount >= 2:
        numberOf2zl += 1
        userAmount -= 2
    else:
        numberOf1zl += 1
        userAmount -= 1

print(f"5 zł - {numberOf5zl} \n2 zł - {numberOf2zl} \n1 zł - {numberOf1zl}")