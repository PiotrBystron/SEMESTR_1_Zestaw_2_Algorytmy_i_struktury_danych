def Bubble_sort(T):
    n=len(T)
    ile=0       # to dodatkowa zmienna liczaca liczbe porownan
    for i in range(n):
        for j in range(0, n-i-1):
            ile +=1
            if T[j] > T[j+1] :
                T[j], T[j+1] = T[j+1], T[j] #zamiana miejscami
    return T,ile

A=[10,51,2,18,4,31,13,5,23,64,29,10,2]
#A=[3,14,15,17,28,31,50,60]
#A=[2,2,2,2,2]
#A=[3,2,1]

print(A)
print(Bubble_sort(A))