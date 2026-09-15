n = int(input("100 gacha bolgan son kiriting: "))
print("3 ga qoldiqsiz bolinadiganlar")
for son in range(1,n):
    if son %3 == 0:
        print(son)
        
        
print ("\n \n5 ga qoldiqsiz bolinadigan sonlar\n")       
for son in range(1,n):
    if son %5 == 0:
        print(son)