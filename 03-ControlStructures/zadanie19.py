dogYears = int(input("Podaj ile lat ma pies: "))
humanYears = 0

while dogYears > 0:
    if dogYears <= 2:
        humanYears += 10.5
        dogYears -= 1
    else:
        humanYears += 4
        dogYears -= 1

print(f"Twój pies ma {humanYears} ludzkich lat")
