
def palindrom_function(S1):
    #S1 = str(input("Enter a String: "))
    S2=""
    for i in S1:
        S2 = i + S2
    if S1 == S2:
        return print("String is Palindrome")
    else:
        return print("String is not Palindrome")

S1 = str(input("Enter a String: "))
palindrom_function(S1)
