# Input the three sides
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

# Check if the sides are greater than zero and can form a triangle
if (side_a > 0) and (side_b > 0) and ( side_c > 0):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("These sides can form a triangle.")
    else:
        print("These sides cannot form a triangle.")
else:
    print("The sides must be greater than zero.")
