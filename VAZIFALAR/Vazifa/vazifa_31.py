student = {
    "Ali":{"Mate":5,
           "Ona":4,
           "ingl":5,
           "fizi":3,
           "nems":4
           },
    
    "Abu":{"Mate":3,
           "Ona":5,
           "ingl":4,
           "fizi":5,
           "nems":3
           },
    
    "Bobur":{"Mate":5,
           "Ona":3,
           "ingl":5,
           "fizi":5,
           "nems":5
           },
    
    "Botir":{"Mate":4,
           "Ona":4,
           "ingl":3,
           "fizi":3,
           "nems":3,
           "music":5
           }
     }

for ism, baho in student.items():
    ort = sum(baho.values())
    print (f'{ism} jami to\'plagan bali: {ort} ball')