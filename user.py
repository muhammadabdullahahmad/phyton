# Get input from user
x = int(input("Enter the base number (x): "))
n = int(input("Enter the number of terms (n): "))

print(f"\nPower Series for base {x} up to {n} terms:")

# Loop to print the power series
for i in range(n):
    print(f"{x}^{i} = {x**i}")
