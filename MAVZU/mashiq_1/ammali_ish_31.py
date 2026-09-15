son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
son3 = int(input("3-sonni kiriting: "))

if son1 >= son2 and son1 >= son3:
    print("Eng katta son:", son1)
elif son2 >= son1 and son2 >= son3:
    print("Eng katta son:", son2)
else:
    print("Eng katta son:", son3)