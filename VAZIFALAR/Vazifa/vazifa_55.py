def obu_havo(boshi, tugash, qadam=1):
    javob = []
    for c in range(boshi, tugash, qadam):
        f = c * 1.8 + 32
        javob.append(round(f, 1))
    return javob


bosh = int(input('Boshlangich harorat kiriting: '))
tug = int(input('Tugash haroratini kiriting: '))
qad = int(input("Qadamini kiriting: "))

daraja = obu_havo(bosh, tug, qad)
print(daraja)