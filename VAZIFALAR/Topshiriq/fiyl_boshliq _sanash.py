with open('matin.txt','r') as file:
    matn = file.read()

belgi = 0
boshliq = 0

for i in matn:
    if i == " ":
        boshliq += 1
    else:
        belgi += 1
        
with open("yangi_matn.txt", 'w') as file:
    file.write(f"belgi - {belgi}\n")
    file.write(f"boshliq - {boshliq}")