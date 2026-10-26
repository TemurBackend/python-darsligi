def max_top(n):   # funksiya ochdik
    if len(n) == 1 :  # listni olchadik va 1 ta element ga teng bolsa 
        print(n,"n son")
        print(n[0], "n0 son")
        return n[0] #list ichida 1 ta element bolsa oshani qaytaramiz
       
    
    max_qolgan = max_top(n[1:])#max qimatga bita element tashab qolgan hammasini olimz 
    print(max_qolgan,"boshlanishi")
    if n[0] > max_qolgan: #
        print(f"{n[0]} {max_qolgan} solishtr")
        print(n[0])
        return n[0]
      
    else:
        print(max_qolgan)
        return max_qolgan
    
a = [1,2,4,65,4,34,5,6,76,4,5]
    
b = max_top(a)
print(b) 