def f(d):
    cars = []
    for i in range(len(d)):
        if d[i][1] == "in":
            cars.append(d[i][0])
        elif d[i][1] == "out":
            for j in range(len(cars)):
                if cars[j] == d[i][0]:
                    cars.pop(j)
                    break
        print(cars)
    return cars


cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

print(f(cars))
