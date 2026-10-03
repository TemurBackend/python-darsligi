cart = [
    {"name": "Laptop", "price": 8000000, "count": 1},
    {"name": "Mouse", "price": 150000, "count": 2},
    {"name": "Keyboard", "price": 30000000, "count": 1}
]
jami = []
for maxsulot in cart:
    summa = maxsulot['price'] * maxsulot['count']
    print(maxsulot['name'], '=', summa)
    
if summa >= 5_000_000:
    print ("Sizga chegirma bor !!!")
