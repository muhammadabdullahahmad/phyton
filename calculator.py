import math

# Define operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error (div by 0)"
def modulus(x, y): return x % y
def power(x, y): return x ** y
def floor_divide(x, y): return x // y
def square_root(x): return math.sqrt(x)
def factorial(x): return math.factorial(int(x))
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x): return math.log(x)
def log10(x): return math.log10(x)

# Input helper
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Display menu
def display_menu():
    print("\nScientific Calculator Menu:")
    print(" 1. Addition           8. Square Root")
    print(" 2. Subtraction        9. Factorial")
    print(" 3. Multiplication    10. Sine")
    print(" 4. Division          11. Cosine")
    print(" 5. Modulus (%)       12. Tangent")
    print(" 6. Power (**)        13. Natural Log (ln)")
    print(" 7. Floor Division    14. Log base 10")
    print(" 0. Exit")

# Main loop
while True:
    display_menu()
    choice = input("\nEnter your choice (0–14): ").strip()

    if choice == '0':
        print("\nThank you for using the calculator. Goodbye!")
        break

    try:
        if choice in ['8', '9', '10', '11', '12', '13', '14']:
            num = get_number_input("Enter the number: ")
            if choice == '8': print(f"√{num} = {square_root(num)}")
            elif choice == '9': print(f"{num}! = {factorial(num)}")
            elif choice == '10': print(f"sin({num}) = {sin(num)}")
            elif choice == '11': print(f"cos({num}) = {cos(num)}")
            elif choice == '12': print(f"tan({num}) = {tan(num)}")
            elif choice == '13': print(f"ln({num}) = {log(num)}")
            elif choice == '14': print(f"log10({num}) = {log10(num)}")
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            if choice == '1': print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2': print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3': print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4': print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5': print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6': print(f"{num1} ** {num2} = {power(num1, num2)}")
            elif choice == '7': print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        else:
            print("Invalid choice. Please enter a number between 0 and 14.")
    except Exception as e:
        print(f"Error: {e}")
