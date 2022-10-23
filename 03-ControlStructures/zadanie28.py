f1 = 0
f2 = 1 
help = 0

for i in range(50):
    print(f1, end = " ")
    help = f1 + f2
    f1 = f2
    f2 = help