# n = int(input('istalgan mon kiriting '))
n = input("Istalgan son kiriting: ")
if n.isdigit():
    n = int(n)
    son = 0
    while son < n:
        son += 1
        print(son)
else:
    print("Siz son kiritmadingiz!")