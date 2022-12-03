import re

mess = "To be, or not to be, that is the question"
vowels = re.findall("[aeiou]", mess)

print(vowels)

count = 0
for i in range(len(vowels)):
    count+=1

print(count)
