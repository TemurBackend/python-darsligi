student = [
    {"name": "Ali", "baholar":[5,4,3,5,4,]},
    {"name": "Abbos", "baholar":[5,3,3,3,3,9,9,9,9,9,9]},
    {"name": "Asad", "baholar":[4,4,3,4,4,]},
    {"name": "Abror", "baholar":[5,5,5,4,5]},
    {"name": "Abu", "baholar":[5,4,3,5]},
    {"name": "Blol", "baholar":[5,4,3,5,4,4]},
    {"name": "Saman", "baholar":[5,4,3,5,4,5]},
    {"name": "Sardor", "baholar":[5,4,3,5,4,3]}
    ]
for oquv in student:
    ism = oquv['name']
    baholar = oquv['baholar']
    orta = round(sum(baholar) / len(baholar), 1)
    if orta >= 4.5:
        print (f'{ism} o\'rtacha bahosi: {orta} Alo')
    elif orta > 3.4:
        print (f'{ism} o\'rtacha bahosi: {orta}-Yahshi')
    else:
        print (f'{ism} o\'rtacha bahosi: {orta} Qoniqarsiz')
     