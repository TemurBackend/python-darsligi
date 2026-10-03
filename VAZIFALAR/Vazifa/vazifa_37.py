employees = {
    "Ali": {
        "age": 25,
        "salary": 5000000,
        "skills": ["Python", "Django"]
    },
    "Vali": {
        "age": 28,
        "salary": 7000000,
        "skills": ["PHP", "Laravel"]
    },
    "Sardor": {
        "age": 23,
        "salary": 4500000,
        "skills": ["Python", "FastAPI"]
    }
}

for x in employees:
    print(x, employees[x]["salary"])

print("6 000 000 dan yuqori:")

for x in employees:
    if employees[x]["salary"] > 6000000:
        print(x)

print("Python biladiganlar:")

for x in employees:
    if "Python" in employees[x]["skills"]:
        print(x)
jami = 0

for x in employees:
    jami += employees[x]["salary"]
orta = jami / len(employees)
print("O'rtacha maosh:", orta)
