def selsiy_to_farengeyt_oraliq(boshlangich, tugash, qadam=1):
    natija = []
    for c in range(boshlangich, tugash, qadam):
        f = c * 1.8 + 32
        natija.append(round(f, 1))
    return natija


f_darajalar = selsiy_to_farengeyt_oraliq(0, 20, 5)
print(f_darajalar)