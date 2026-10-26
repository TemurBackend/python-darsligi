# factorial(5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)

def factorial(n):
    if n == 1:
        return n
    
    return n*factorial(n-1)


print(factorial(5))