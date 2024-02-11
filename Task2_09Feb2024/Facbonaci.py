import math
num = int(input("Enter a number: "))
a , b = 0, 1
print("Fibonaci Series: ", a, end=" ")
for i in range(0,num-1):
    c = a+b
    a=b
    b=c
    print( c, end=" ")



