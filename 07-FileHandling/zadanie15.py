file = open("lorem.txt", "r", encoding="utf-8")
count = 1
for i in file:
    print(i)
    if(count % 5 == 0):
        enter = input("Press enter to continue: ")
        print()
    count+=1

file.close()
    

