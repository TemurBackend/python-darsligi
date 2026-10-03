orders = [
    {
        "customer": "Ali",
        "items": [
            {"name": "Mouse", "price": 150000},
            {"name": "Keyboard", "price": 300000}
        ]
    },
    {
        "customer": "Vali",
        "items": [
            {"name": "Laptop", "price": 8000000}
        ]
    }
]
for bu in orders:
    jami = 0
    for s in bu['items']:
        jami += s['price']
    print(bu['customer'], ':', jami)