import stackImport
import operator

stack = []

expr = input("Podaj działanie: ")

allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
    }

for i in expr:
    if ord(i) > 47 and ord(i) < 58:
        stackImport.push(stack, i)
    elif i == "-" or i == "+" or i == "*" or i == "/" or i == "^":
        x = int(stackImport.pop(stack))
        y = int(stackImport.pop(stack))
        result = allowed_operators[i](y,x)
        stackImport.push(stack, result)
    else:
        print(stackImport.pop(stack))

 