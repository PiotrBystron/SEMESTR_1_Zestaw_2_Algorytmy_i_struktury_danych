def tribonacii(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return tribonacii(n-1)+tribonacii(n-2)+tribonacii(n-3)

for i in range(7):
    print(i,tribonacii(i))
