def facto_function(num):
    for i in range(1, num):
        num = num * i
        i = i + 1
    return(num)
num = int(input("Enter a number:"))
facto = facto_function(num)
print("Factorial of number is: ",facto)
