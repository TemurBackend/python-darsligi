narh = 15000
choy = True
salat = True

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000

print (f"Jami {narh} so'm ")