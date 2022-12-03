import stackImport

stack = []
division = 18
binary = ""

while division > 0:
    rest = division % 2
    stackImport.push(stack,rest)
    division = int(division / 2)


for i in range(len(stack) - 1, -1, -1):
    binary = binary + str(stack[i])

print("binary num is: ", binary)
