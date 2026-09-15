narx = float(input("Mahsulot narxini kiriting: "))

if narx <= 100000:
    chegirma = 0
elif narx <= 500000:
    chegirma = 5
elif narx <= 1000000:
    chegirma = 10
else:
    chegirma = 15

chegirma_summasi = narx * chegirma / 100
yakuniy_narx = narx - chegirma_summasi

print("Chegirma:", chegirma, "%")
print("Chegirmadan keyingi narx:", yakuniy_narx)