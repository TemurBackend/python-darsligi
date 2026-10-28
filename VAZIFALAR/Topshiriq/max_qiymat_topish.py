def max_top(n):   
    if len(n) == 1 : 
        return n[0] 
       
    max_qolgan = max_top(n[1:])
    if n[0] > max_qolgan: #
        return n[0]
      
    else:
        return max_qolgan
    
a = [1,2,4,65,4,34,5,6,76,4,5]
    
b = max_top(a)
print(b) 