import re

mess = "To be , or not to be, that is the question"
words = re.findall("\w+", mess)

print(words)

count = 0
for i in range(len(words)):
    count+=1

print(count)