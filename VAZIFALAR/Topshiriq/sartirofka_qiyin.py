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
[]
{}
()


ismlar = [
    "Osimxon",
    "Anasxon",
    "Abdulaziz",
    "Abdullayev MuhammadAmin",
    "Temurbek",
    "Vali",
    "Otabek",
    "Muslim",    
    "Abdullayev MuhammadAli",
    "Nematjon"
]    





def tartib(ismlar):
    n = len(ismlar)
    for i in range(n):
        for j in range(n):
            
            if A[ismlar[i][0]] < A[ismlar[j][0]]:
                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                if A[ismlar[i][0]] == A[ismlar[j][0]]:
                    if A[ismlar[i][1]] == A[ismlar[j][1]]:
                        if A[ismlar[i][2]] == A[ismlar[j][2]]:
                            if A[ismlar[i][3]] == A[ismlar[j][3]]:
                                if A[ismlar[i][4]] == A[ismlar[j][4]]:
                                    if A[ismlar[i][5]] == A[ismlar[j][5]]:
                                        if A[ismlar[i][6]] == A[ismlar[j][6]]:
                                            if A[ismlar[i][7]] == A[ismlar[j][7]]:
                                                if A[ismlar[i][8]] == A[ismlar[j][8]]:
                                                    if A[ismlar[i][9]] == A[ismlar[j][9]]:
                                                        if A[ismlar[i][10]] == A[ismlar[j][10]]:
                                                            if A[ismlar[i][11]] == A[ismlar[j][11]]:
                                                                if A[ismlar[i][12]] == A[ismlar[j][12]]:
                                                                    if A[ismlar[i][13]] == A[ismlar[j][13]]:
                                                                        if A[ismlar[i][14]] == A[ismlar[j][14]]:
                                                                            if A[ismlar[i][15]] == A[ismlar[j][15]]:
                                                                                if A[ismlar[i][16]] == A[ismlar[j][16]]:
                                                                                     if A[ismlar[i][17]] == A[ismlar[j][17]]:
                                                                                         if A[ismlar[i][18]] == A[ismlar[j][18]]:
                                                                                             if A[ismlar[i][19]] == A[ismlar[j][19]]:
                                                                                                 if A[ismlar[i][20]] == A[ismlar[j][20]]:
                                                                                                     if A[ismlar[i][21]] == A[ismlar[j][21]]:
                                                                                                         if A[ismlar[i][22]] == A[ismlar[j][22]]:
                                                                                                             if A[ismlar[i][23]] == A[ismlar[j][23]]:
                                                                                                                 break
                                                                                                         else:
                                                                                                             if A[ismlar[i][23]] < A[ismlar[j][23]]:
                                                                                                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]       
                                                                                                     else:
                                                                                                         if A[ismlar[i][22]] < A[ismlar[j][22]]:
                                                                                                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]              
                                                                                                 else:
                                                                                                     if A[ismlar[i][21]] < A[ismlar[j][21]]:
                                                                                                        ismlar[i], ismlar[j] = ismlar[j], ismlar[i]   
                                                                                             else:
                                                                                                 if A[ismlar[i][20]] < A[ismlar[j][20]]:
                                                                                                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]        
                                                                                         else:
                                                                                             if A[ismlar[i][19]] < A[ismlar[j][19]]:
                                                                                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]            
                                                                                     else:
                                                                                         if A[ismlar[i][18]] < A[ismlar[j][18]]:
                                                                                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]                
                                                                                else:
                                                                                    if A[ismlar[i][17]] < A[ismlar[j][17]]:
                                                                                       ismlar[i], ismlar[j] = ismlar[j], ismlar[i]         
                                                                            else:
                                                                                if A[ismlar[i][16]] < A[ismlar[j][16]]:
                                                                                     ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                                                                        else:
                                                                            if A[ismlar[i][15]] < A[ismlar[j][15]]:
                                                                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                                                                    else:
                                                                        if A[ismlar[i][14]] < A[ismlar[j][14]]:
                                                                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]    
                                                                else:
                                                                    if A[ismlar[i][13]] < A[ismlar[j][13]]:
                                                                        ismlar[i], ismlar[j] = ismlar[j], ismlar[i]        
                                                            else:
                                                                if A[ismlar[i][12]] < A[ismlar[j][12]]:
                                                                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]            
                                                        else:
                                                            if A[ismlar[i][11]] < A[ismlar[j][11]]:
                                                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]                
                                                    else:
                                                        if A[ismlar[i][10]] < A[ismlar[j][10]]:
                                                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]                   
                                                else:
                                                    if A[ismlar[i][9]] < A[ismlar[j][9]]:
                                                        ismlar[i], ismlar[j] = ismlar[j], ismlar[i]                           
                                            else:
                                                if A[ismlar[i][8]] < A[ismlar[j][8]]:
                                                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]                                    
                                        else:
                                            if A[ismlar[i][7]] < A[ismlar[j][7]]:
                                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                                    else:
                                        if A[ismlar[i][6]] < A[ismlar[j][6]]:
                                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                                else:
                                    if A[ismlar[i][5]] < A[ismlar[j][5]]:
                                        ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                            else:
                                if A[ismlar[i][4]] < A[ismlar[j][4]]:
                                    ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                        else:
                            if A[ismlar[i][3]] < A[ismlar[j][3]]:
                                ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                    else:
                        if A[ismlar[i][2]] < A[ismlar[j][2]]:
                            ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                else:
                    if A[ismlar[i][1]] < A[ismlar[j][1]]:
                        ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
            
    return ismlar       
            
            
            

            
            
            
            
            
            
            
print(tartib(ismlar))

# def tartib(ismlar):
#     n = len(ismlar)
#     for i in range(n):
#         for j in range(n):
#             if A[ismlar[i][0]] < A[ismlar[j][0]]:
#                 ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
                
#             if A[ismlar[i][0]] == A[ismlar[j][0]]:
#                 n,m = len(ismlar[i]), len(ismlar[j])
#                 if n < m:
#                     ismlar[i], ismlar[j] = ismlar[j], ismlar[i]
#     return ismlar       



