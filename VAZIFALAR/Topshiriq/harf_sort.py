A = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
    "a": 26,
    "b": 27,
    "c": 28,
    "d": 29,
    "e": 30,
    "f": 31,
    "g": 32,
    "h": 33,
    "i": 34,
    "j": 35,
    "k": 36,
    "l": 37,
    "m": 38,
    "n": 39,
    "o": 40,
    "p": 41,
    "q": 42,
    "r": 43,
    "s": 44,
    "t": 45,
    "u": 46,
    "v": 47,
    "w": 48,
    "x": 49,
    "y": 50,
    "z": 51,
}

# a = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O',
#     'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C',
#     'B', 'A',
#     'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o',
#     'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c',
#     'b', 'a', "9"]
# def sar(arr):
#     s = 0
#     for harf in arr:
#         y = 0
#         for j in arr:
#             if A[harf] < A[j]:
#                 arr[s], arr[y] = arr[y], arr[s]
#             y +=1
#         s +=1     
#     return arr   

# print(sar(a))



ismlar = [
    ["Osimxon"],
    ["Anasxon"],
    ["Abdulaziz"],
    ["Temurbek"],
    ["Vali"],
    ["Otabek"],
    ["Muslim"],
    ["Nematjon"]
]    

n = len(ismlar)

for i in range(n):
    for j in range(n):
        if A[ismlar[i][0][0]] < A[ismlar[j][0][0]]:
            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
            
print(ismlar)

















