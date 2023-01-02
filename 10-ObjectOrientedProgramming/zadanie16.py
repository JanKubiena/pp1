class bank_account():
    def __init__(self, bank_no):
        self.user_bank_no = bank_no
        self.user_balance = 0
    def deposit(self, how_much):
        self.user_balance += how_much
    def widthdraw(self, how_much):
        if how_much <= self.user_balance:
            self.user_balance -= how_much
        else:
            print("not enough balance on your account!")  
    def display_balance(self):
        print(f"Bank Accoun No: {self.user_bank_no}\n Balance: PLN {self.user_balance}")

acc = bank_account("12 3456 5555 9090 1111 0000 7722")
acc.display_balance()
acc.deposit(25.30)
acc.display_balance()
acc.widthdraw(31.70)
acc.display_balance()
acc.widthdraw(14)
acc.display_balance()

