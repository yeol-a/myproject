
def selectionSort(L):
    for i in range(0, len(L)):
        smallest=i
        for j in range(i+1, len(L)):
            if L[smallest] > L[j]:
                smallest=j
        L[smallest], L[j] = L[j], L[smallest]
                
