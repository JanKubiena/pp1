arr = ["Harry Potter", "Hobbit", "auta", "auta 2", "auta 3"]
file = open('filmy.txt','w',encoding="utf-8") 

for i  in arr:
    file.write(i+"\n")

file.close()
