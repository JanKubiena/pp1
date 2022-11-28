phone = {
    "firm": "Apple",
    "model": 13,
    "size": "8 inches",
    "applications": ["settings","appstore"],
    "working": True,
    "number":{"landline":"123444321","mobile":"777888999"}
   }

for i in phone:
    print(i,": ",phone[i])

for k,v in phone.items():
    print(k,v)
    