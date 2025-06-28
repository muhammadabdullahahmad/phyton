def is_natural_number(num):
    try:
        # Convert the input to a float first to handle both integer and decimal inputs
        number = float(num)
        
        # Check if the number is an integer and greater than 0
        if number.is_integer() and number > 0:
            return True
        else:
            return False
    except ValueError:
        # If conversion to float fails, it's not a number
        return False

# Get user input
user_input = input("Enter a number to check if it's a natural number: ")

# Check and display result
if is_natural_number(user_input):
    print(f"'{user_input}' is a natural number.")
else:
    print(f"'{user_input}' is NOT a natural number.")