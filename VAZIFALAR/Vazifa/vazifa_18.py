tav = ['Non', 'Sut', 'Go\'sht']
nar =  [3500, 9000, 85000]
miq = [2, 1.5, 1]

som = nar[0] * miq[0]
som1 = nar[1] * miq[1]
som2 = nar[2] * miq[2]

jam = som + som1 + som2 

qqs = jam * 12 / 100

pu = jam + qqs
 

print("          KASSA CHEKI         ")
print(f'{tav[0]}; {miq[0]}ta; {nar[0]} narhi; {som} SOM  ')
print(f'{tav[1]}; {miq[1]}litr; {nar[1]} narhi; {som1} SOM  ')
print(f'{tav[2]}; {miq[2]}ta; {nar[2]} narhi; {som2} SOM  ')
print("\n")

print(f"Jami: {jam:} so'm")
print(f"QQS 12%: {qqs:} so'm")
print(f"To'lov: {pu: } so'm")