import json

phone = {
    "firm": "Apple",
    "model": 13,
    "size": "8 inches",
    "applications": ["settings","appstore"],
    "working": True,
    "number":{"landline":"123444321","mobile":"777888999"}
   }
with open("jp2.json", "w") as f:
    json.dump(phone, f, indent = 6)