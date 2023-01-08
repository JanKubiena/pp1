class C():

    @staticmethod
    def m1(n):
        string = str(n)
        arr = []
        result = ""
        for i in string:
            if i != "1" and i != "3" and i != "5" and i != "7" and i != "9":
                arr.append(i)

        for i in arr:
            result += i

        return int(result)

    @staticmethod
    def m2(n):
        string = str(n)
        arr = []
        for i in range(len(string) -1):
            if int(string[i]) > int(string[i+1]):
                return False
        return True

    @staticmethod
    def m3(n):
        string = str(n)
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        result = ""
        counter = 0

        for i in range(len(string)):
            for j in range(len(numbers)):
                if string[i] == numbers[j - counter]:
                    numbers.pop(j - counter)
                    counter += 1
                    break
                else:
                    continue

        for j in range(len(numbers)):
                result += numbers[j]

        return result


print(C.m1(4231564)) 
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))
