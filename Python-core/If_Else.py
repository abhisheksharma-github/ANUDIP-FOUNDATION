# Input the three sides
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

# Check if the sides are greater than zero and can form a triangle
if (side_a > 0) and (side_b > 0) and (side_c > 0):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        print("These sides can form a triangle.")

        # Determine the type of triangle
        if side_a == side_b == side_c:
            print("The triangle is Equilateral.")
        elif side_a == side_b or side_b == side_c or side_a == side_c:
            print("The triangle is Isosceles.")
        else:
            print("The triangle is Scalene.")
        
        # Check if it is also a Right-Angled Triangle
        if (side_a**2 == side_b**2 + side_c**2 or 
            side_b**2 == side_a**2 + side_c**2 or 
            side_c**2 == side_a**2 + side_b**2):
            print("The triangle is also Right-Angled.")
            
    else:
        print("These sides cannot form a triangle.")
