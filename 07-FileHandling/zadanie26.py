import re

with open("lorem.txt") as file:
    file_content = file.read()

words = re.findall("\w+", file_content)

for i in range(len(words)):
    if len(words[i])  >= 6:
        print(words[i])

