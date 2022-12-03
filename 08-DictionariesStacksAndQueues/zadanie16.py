import json

with open("students.json", "r") as f:
    students = json.load(f)

limited_students = []
for student in students:
    limited_student = {
        "id": student["id"],
        "first_name": student["first_name"],
        "last_name": student["last_name"]   
    }
    limited_students.append(limited_student)

with open("limited.json", "w") as f:
    json.dump(limited_students, f, indent=4)
 