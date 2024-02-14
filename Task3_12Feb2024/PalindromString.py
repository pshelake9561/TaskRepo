S1 = str(input("Enter a String: "))
S2=""
for i in S1:
    S2 = i + S2
if S1 == S2:
    print("String is Palindrome")
else:
    print("String is not Palindrome")