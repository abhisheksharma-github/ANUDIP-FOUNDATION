# Input the three sides
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

# Check if they can form a triangle
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")
