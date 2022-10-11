import math

userHeight = float(input('Podaj swój wzrost w cm: '))
userWeight = float(input('Podaj swoją wagę w kg: '))

BMI = userWeight / math.pow((userHeight / 100), 2)

print("Twoje BMI wynosi:", round(BMI, 2))