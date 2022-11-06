def howManyLetter(sentence, letter):
    counter = 0
    for i in sentence:
        if(i == letter):
            counter += 1

    return counter

print(howManyLetter("You never get a second chance to make a first impression", "e"))