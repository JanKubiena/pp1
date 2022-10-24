def keypadNumbers():
    for i in range(1,4):
        for j in range(3,0, -1):
            print(i*3 - j+1, end=" ")
        print()

keypadNumbers()