mahsulot = [
    {"name": "Olma", "narhi": 12000, "soni": 5},
    {"name": "Banan", "narhi": 18000, "soni": 3},
    {"name": "Nok", "narhi": 15000, "soni": 7}
]
for nom in mahsulot:
    jam = nom['narhi'] * nom['soni']
    print (f"{nom['name']}-{jam} so'm")