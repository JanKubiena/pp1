class tv():
    def __init__(self):
        self.is_on =  False
        self.channel_no = 1
        self.channel_list = []
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
    def set_channel_no(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels):
        self.channel_list = channels
    def show_channels(self):
        print(self.channel_list)
    def show_channel_name_on_no(self,no):
        if no > len(self.channel_list):
            print("No channel under this number :(")
        else:
         print(self.channel_list[no - 1])


tv1 = tv()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()
tv1.turn_on()
tv1.set_channel_no(5)
tv1.show_status()
tv1.show_channels()
tv1.set_channels(["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
tv1.show_channels()
tv1.show_channel_name_on_no(6)