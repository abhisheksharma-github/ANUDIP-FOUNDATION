# Input the three sides
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

# Check if they can form a triangle
if a + b > c and a + c > b and b + c > a:
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")
