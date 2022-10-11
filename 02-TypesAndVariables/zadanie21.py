import random

diceNumber = random.randrange(1, 7)

userNumber = int(input("Zgadnij co wypadło na kostce: "))

if userNumber == diceNumber:
    print("Zgadłeś!")
else:
    print("Niezgadłeś!")
    

