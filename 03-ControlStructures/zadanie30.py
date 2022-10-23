N = int(input("Podaj liczbe którą chcesz sprawdzić czy jest pierwsza: "))

if N > 1:
    flag = True
else:
    flag = False

for i in range(2,int(N/2 + 1)):
    if N % i == 0:
        flag = False
        break

if flag == True:
    print("Liczba jest pierwsza")
else:
    print("Liczba NIE jest pierwsza")

