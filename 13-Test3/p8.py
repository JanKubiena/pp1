class C():

    def __init__(self, dict):
        self.grades = dict

    def m(self, n):
        result = ""
        arr = []
        for k,v in self.grades.items():
            sum = 0
            counter = 0
            for i in v:
                sum += i
                counter += 1
            avg = sum / counter
            if avg >= n:
                arr.append(k)

        arr.sort()

        for i in arr:
            result = result + i + ","

        result = result[:-1]

        return result

grades = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})

print(grades.m(4))
print(grades.m(3))
print(grades.m(5))

print()