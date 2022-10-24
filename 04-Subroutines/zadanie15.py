import myMath

userNum = 0

while userNum != myMath.drawRandom():
    userNum = myMath.read_number()

print(f"{userNum} - Zgadłeś!")
