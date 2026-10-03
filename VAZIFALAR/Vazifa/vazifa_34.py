menu = {
    "Pizza": {
        "price": 50000,
        "ingredients": ["cheese", "tomato", "meat"]
    },
    "Burger": {
        "price": 35000,
        "ingredients": ["bread", "meat", "cheese"]
    },
    "Salad": {
        "price": 25000,
        "ingredients": ["tomato", "cucumber"]
    }
}
print(' "Pishloqli mahsulotimmiz" ')
for ma in menu:
    if 'cheese' in menu[ma]['ingredients']:
        print(ma)
    else:
        print (' "Pishloqsiz mahsulotimmiz" \n',ma)

for ma in  menu:
    if  menu[ma]['price'] > 40000:
        print('"Narhi 40000 So\'m dan qimmat bolgan mahsulotimmiz"\n',ma)