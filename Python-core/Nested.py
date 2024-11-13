# Taking three numbers as input 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

print("First Number is :",num1)
print("Second Number is :",num2)
print("Third Number:is ",num3)
# Finding the greatest number using nested if-else Condition
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
print("Greatest number is:", greatest)
