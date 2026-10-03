test = [
    "Haftada necha kun bor?",
    "Bir yilda necha oy bor?",
    "O'zbekiston poytaxti qaysi shahar?",
    "Quyosh qayerdan chiqadi?",
    "45 -  17",
    "qayerdamiz?"
]

javob = [
    "7",
    "12",
    "toshkent",
    "sharq",
    "28"
]

answer_count = len(javob)
test_count = len(test)

if answer_count != test_count:
    print("Testlar va javoblar soni bir biriga to'g'ri kelmayapti!")
    

i = 0
ball = 0


while i < test_count:
    print(test[i])
    javo = input("Javob: ")

    if javo.lower() == javob[i]:
        print("To'g'ri!")
        ball += 1
    else:
        print("Noto'g'ri!")

    i += 1

print("Siz ", test_count, " ta savoldan", ball, "tasiga to'g'ri javob berdingiz.")
print("Ball:", ball, "/", test_count)
