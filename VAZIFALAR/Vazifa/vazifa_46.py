son = 0
jam = 0

while True:
    baho = int(input("Baho: "))

    if baho == -1:
        break

    jam += baho
    son += 1

if son > 0:
    orta = jam / son
else:
    orta = 0

print("Kiritilgan baholar soni:", son)
print("Jami ball:", jam)
print("O‘rtacha baho:", orta)