def sumOfDigits(n):
    sum = 0
    digit = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = int(n / 10)

    return sum

print(sumOfDigits(7182))
