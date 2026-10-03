balance = 500000
jam = 0

while True:
    narh = int(input("Mahsulot narxi: "))
    if narh == 0:
        break
    if narh <= balance:
        balance -= narh
        jam += narh
        print("Xarid qilindi")
    else:
        print("Pul yetarli emas")
print("Jami xarajat:", jam)
print("Qolgan balans:", balance)
