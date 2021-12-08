def SelectionSort(T):
    n=len(T)
    ile_porownan = 0  # to dodatkowa zmienna liczaca liczbe porownan
    for i in range(n-1):
        min=i
        for j in range(i + 1,n):
            ile_porownan +=1
            if T[j] < T[min]:
                min = j
        tmp=T[i]
        T[i]=T[min]
        T[min]=tmp
    return T,ile_porownan

#A=[10,51,2,18,4,31,13,5,23,64,29,10,2]
A=[3,14,15,17,28,31,50,60]
print(A)
print(SelectionSort(A))