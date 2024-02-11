side1 = int(input("Enter side1 value: "))
side2 = int(input("Enter side2 value: "))
side3 = int(input("Enter side3 value: "))
if side1 == side2 and side2 == side3 and side1 == side3:
    print("The triangle is equilateral")
elif side1 == side2 and side1 != side3 or side1 == side3 and side1 != side2:
    print("The triangle is isosceles")
else:
    print("The triangle is Scalane")
