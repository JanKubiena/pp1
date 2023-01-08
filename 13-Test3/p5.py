class C():
    def __init__(self, arr):
        self.intigers = arr
        self.string = ""
        self.sum = 0

    def __str__(self):
        for i in range(len(self.intigers)):
            self.string = self.string + str(self.intigers[i]) + "+"

        self.string = self.string[:-1]

        for i in range(len(self.intigers)):
            self.sum += self.intigers[i]

        return f"{self.string}={self.sum}"

ex = C([6,0,15])
print(ex)