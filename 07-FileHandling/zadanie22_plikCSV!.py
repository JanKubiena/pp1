import csv
with open("students.csv", newline="") as csvfile:
    data = csv.DictReader(csvfile)

    for line in data:
        if int(line["age"]) < 30:
            print(line["first_name"]," ", line["last_name"]," ", line["email"]) 

csvfile.close()


