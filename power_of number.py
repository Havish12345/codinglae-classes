

base = int(input("Enter base number: "))

exponent = int(input("Enter exponent: "))

result = 1 # Start with 1 because anything raised to power 0 is 1

for _ in range(exponent):

 result *= base # Multiply base with result in each iteration

print(f"{base} raised to the power {exponent} is: {result}")
