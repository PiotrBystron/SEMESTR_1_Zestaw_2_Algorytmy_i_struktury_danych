def InsertionSort(T):
    n=len(T)
    ile_porownan=0       # to dodatkowa zmienna liczaca liczbe porownan
    for i in range(1,n):
        key = T[i]
        j=i-1
        while j>-1 and key < T[j]:
            ile_porownan +=1
            T[j+1]=T[j]
            j = j-1
        if j>-1:
            ile_porownan +=1
        T[j+1]=key
    return T,ile_porownan

#A=[10,51,2,18,4,31,13,5,23,64,29,10,2]
#A=[3,14,15,17,28,31,50,60]
A=[2,1,2,6,2,2,9,2]
print(A)
print(InsertionSort(A))