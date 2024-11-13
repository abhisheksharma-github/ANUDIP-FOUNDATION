# Taking three numbers as input 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print("First Number:,num1")
print("Second Number:,num2")
print("Third Number:,num3")
# Finding the greatest number using nested if-else
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3

#result
print("The greatest number is:", greatest)
