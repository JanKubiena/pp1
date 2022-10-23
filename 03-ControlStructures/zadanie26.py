from operator import truediv


pin = "0805"
userPin = input("Podaj swój pin: ")
tries = 1

if len(userPin) != 4:
    print("podaj poprawny pin!!!")
    quit()

while(tries < 3):
    if pin != userPin:
        tries += 1
        flag = False
        userPin = input("niepoprawny kod podaj jeszcze raz: ")
    else:
        flag = True
        break

    

if flag == True:
    print("Pin poprawny")
else:
    print("Twoja karta została zablokowana!")        

    


