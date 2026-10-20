def factorial(n):
    natija = 1

    for i in range(1, n + 1):
        print(f"Avval: i = {i}, natija = {natija}, n = {n}")
        natija *= i
        print(f"Keyin: i = {i}, natija = {natija}, n = {n}")
        print("="*20)

    return natija

print(factorial(5))
lll = []

def factorial(n):

    if n == 1:
        return 1
    print("N=", n)
    result = n * factorial(n - 1)
    print("Result: ", result) # 6 * 5 * 4 * 3 * 2 * 1

    return result

print(factorial(6))



def son_kiriting(savol):
    son = input(savol)
    while son.isdigit() != True:
        son = input(savol)
    return int(son)


N = son_kiriting("N sonini kiriting: ")