#QUESTION NO 1
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))15


si = (p * r * t) / 100
print("Simple Interest:", si)
print("--------NEXT QUESTION------")

#QUESTION NO 2
p = float(input("Principal : "))
r = float(input("Rate: "))
t = float(input("Time: "))

ci = p * (1 + r / 100) ** t - p
print("Compound Interest:", ci)
print("--------NEXT QUESTION------")
#QUESTION NO 3
cost = float(input("Enter Cost Price: "))

discounted_price = cost * 0.8
print("Price after 20% discount:", discounted_price)
print("--------NEXT QUESTION------")
#QUESTION NO 4
c = float(input("Temperature in Celsius: "))

f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)
