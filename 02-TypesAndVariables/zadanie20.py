import random

sumOfDiceRolls = 0
diceNumber = 0

for x in range(3):
    diceNumber = random.randrange(1, 7)
    print(diceNumber)
    sumOfDiceRolls = sumOfDiceRolls + diceNumber


print("Suma oczek na wyrzuconych kostkach: ", sumOfDiceRolls)