def tez(arr):
    for i in range(len(arr) - 1):
        mini = i
        
        for j in range(i + 1, len(arr)):
            if arr[mini] > arr[j]:
                mini = j
            
        if mini != i:
            arr[mini], arr[i] = arr[1], arr[mini]
    return arr

hh = [7,6,4,2]

print(hh)

print( tez(hh))
