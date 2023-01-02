class statistics():
    def __init__(self, numbers):
        self.user_numbers = numbers
        self.max = None
        self.min = None
        self.arithmetic__mean = None
        self.median_ = None
    def display_numbers(self):
        for i in self.user_numbers:
            print(i, end=" ")
        print()
    def greatest(self):
        max = 0
        for i in self.user_numbers:
            if i > max:
                max = i
        self.max = max
    def smallest(self):
        min = self.user_numbers[0]
        for i in self.user_numbers:
            if i < min:
                min = i
        self.min = min
    def arithmetic_mean(self):
        sum = 0
        count = 0
        for i in self.user_numbers:
            sum += i
            count += 1

        mean = (sum / count)
        self.arithmetic__mean = mean
    def median(self):
        lenght = len(self.user_numbers)
        sort = sorted(self.user_numbers)
        if lenght % 2 == 0:
            median = (sort[int(lenght/2)] + int(sort[int(lenght/2) - 1])) /  2
        else:
            median = int(sort[int(lenght/2)])

        self.median_ = median
    def display_results(self):
        print(f"max: {self.max}\nmin: {self.min}\narithetic mean: {self.arithmetic__mean}\nmedian: {self.median_}")


num = statistics([1,1,2,2,2,2,1,1])
num.display_numbers()
num.greatest()
num.smallest()
num.arithmetic_mean()
num.median()
num.display_results()
