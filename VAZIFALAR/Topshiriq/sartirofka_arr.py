hh = [6,2,3,412,3,2,4,3,112,3,43,34,656,57,6,323]


def Sartirofka(lis):
    son = 0
    for _ in lis:
        print(f"katta for, qadam = {son}, hozirgi son = {lis[son]}, \nList = {lis}")
        ind = 0
        for i in lis:
            print(f"kichik for, qadam = {ind},hozirgi son = {lis[son]}, \nList = {lis}")
            if lis[son] < lis[ind]:
                temp = lis[son]
                lis[son] = lis[ind]
                lis[ind] = temp 
            ind += 1
        son += 1
    return lis
print(Sartirofka(hh))