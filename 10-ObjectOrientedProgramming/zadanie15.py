import random

class termometre():
    def __init__(self):
        self.user_temp = 36.6
        self.is_on = False
    def turn_on(self):
        if self.is_on == False:
            self.is_on = True
    def turn_off(self):
        if self.is_on:
            self.is_on = False 
    def mesure_temp(self, temp):
        self.user_temp = temp
    def display_temp(self):
        print(f"Temperature: {self.user_temp}C", end = " ")
        if self.user_temp >= 37 and self.user_temp < 41:
            print("(fever)")
        if self.user_temp >= 41:
            print("(CRITICAL TEMPERATURE!!!)")
       

temp = round(random.uniform(34,42), 1)
termo = termometre()
termo.turn_on()
termo.mesure_temp(temp)
termo.display_temp()
termo.turn_off()
