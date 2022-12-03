import json

with open("eurValue.json", "r") as f:
    rates = json.load(f)

table = []
for i in rates:
    rate = {
    "effectiveDate" : i["effectiveDate"],
    "bid" : i["bid"],
    "ask" : i["ask"]
    }
    table.append(rate)
print("date             buing rate  selling rate")
print("=========================================")

for i in range(len(table)):
    for k,v in table[i].items():
        print(v, end="       ")
    print()

   

