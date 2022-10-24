def displayIntigers(N):
    for i in range(1, N+1):
        print(i, end=" ")

N = int(input("podaj N: "))

displayIntigers(N)
print()
displayIntigers(N+10)