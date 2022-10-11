import math

a = float(input('podaj długość pierwszego boku trójkąta: '))
b = float(input('podaj długość drugiego boku trójkąta: '))
c = float(input('podaj długość trzeciego boku trójkąta: '))
s = (a+b+c)/2

Area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('pole twojego trójkąta wynosi: ', Area)
