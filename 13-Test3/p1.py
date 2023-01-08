def f(n):
    sticks = ""
    for i in range(n):
        if i % 5 == 0 and i != 0:
            sticks = sticks + "-/"
        else:
            sticks = sticks + "/"

    return sticks

print(f(57))