son = int(input("4 xonali butun son kiriting: "))
         
ming = son // 1000
yuz = (son // 100) %10
onl = (son // 10 ) % 10
bir = son % 10


yig = ming + yuz + onl + bir
tes = ming * 1000 + yuz * 100 + onl * 10 + bir

print ("Minglar:", ming)
print ("Yuzlar:", yuz)
print ("O'nliklar:", onl)
print ("Birlar:", bir)
print ("Yig'indi:", yig)
 
tes =int(str(tes)[::-1])
print("Teskari tartibi:",tes)