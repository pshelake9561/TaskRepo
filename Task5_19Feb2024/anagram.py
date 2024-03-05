def substring(St1, St2):
    st3 = " "
    for i in St1:
        for j in St2:
            if i == j:
                st3 = st3 + j

    if St2 == st3:
        print("Second string is substring of First string")
    else:
        print("Second string is not substring of First string")


St1 = str(input("Enter First String: "))
St2 = str(input("Enter Second String: "))
substring(St1, St2)

