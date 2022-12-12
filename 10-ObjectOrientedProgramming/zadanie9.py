class tv():
    def __init__(self):
        self.is_on =  False
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print("TV is ON")
            print(f"Channel number is: {self.channel_no}")
        else:
            print("TV is OFF") 

tv1 = tv()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()