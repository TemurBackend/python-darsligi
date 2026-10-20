def yigindi(n):
    if n < 10:
        return n

    return n % 10 + yigindi(n // 10)

yigindi(123456789)

def kopaytma(n):
    if n < 10:
        return n

    return n % 10 * kopaytma(n // 10)

print(kopaytma(1)) 

def juft_yigindi(n):
    if n < 10:
        return n 
    
    raqam = n % 10

    if raqam % 2 == 0:
        return raqam + juft_yigindi(n // 10)
    else:
        return 0 + juft_yigindi(n // 10)
    
juft_yigindi(894651320885)

def maksimali(n):
    if n < 10:
        return n 
    
    raqam = n % 10
    return max(raqam, maksimali(n // 10))

maksimali(987456)

def minimal(n):
    if n < 10:
        return n 
    
    raqam = n % 10
    return min(raqam, minimal(n // 10))

minimal(987456)


def toq_yigindi(n):
    if n < 10:
        return n 
    
    raqam = n % 10

    if raqam % 2 != 0:
        return raqam + toq_yigindi(n // 10)
    else:
        return 0 + toq_yigindi(n // 10)
    
toq_yigindi(3579)
    
    