class substring_program:
    def substr(st1, st2):
        st = " "
        for i in st1:
            for j in st2:
                if i == j:
                    st = st + j
        if st2 == st:
            print("String is substring")
        else:
            print("String is not substring")

    st1 = str(input("Enter first string: "))
    st2 = str(input("Enter second string: "))
    substr(st1, st2)

