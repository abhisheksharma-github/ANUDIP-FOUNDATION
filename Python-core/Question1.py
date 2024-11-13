# Input the three sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check if they can form a triangle
if a + b > c and a + c > b and b + c > a:
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")
