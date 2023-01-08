class cellPhone():
    def __init__(self, make, model, code):
        self.make = make
        self.model = model
        self.code = code
        self.is_on = False
        self.is_unlocked = False

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
        self.is_unlocked = False

    def unlock(self, code):

        if self.is_on == True:
            if self.code == code:
                print(f"code {code} is correct!")
                self.is_unlocked = True
            else:
                print(f"code {code} is incorrect, try again!")
        else:
            print("Firstly turn phone on!")
    
    def status(self):
        print(f"is on?: {self.is_on}, is unlocked?: {self.is_unlocked}")

    def __str__(self):
        return f"make: {self.make}\nmodel: {self.model}"

iphone = cellPhone("Apple", "14-Pro", 1234)
print(iphone)
iphone.unlock(1234)
iphone.turn_on()
iphone.status()
iphone.unlock(1234)
iphone.status()