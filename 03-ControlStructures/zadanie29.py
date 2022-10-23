userNumber = int(input("Podaj liczbe: "))

sum = 0
counter = 0

while(userNumber != 0):
    sum += userNumber
    counter += 1
    userNumber = int(input("Podaj liczbe: "))

mean = sum / counter

print(f"ilość podanych liczb = {counter} \nsuma liczb = {sum} \nsrednia arytmetyczna = {mean}")
