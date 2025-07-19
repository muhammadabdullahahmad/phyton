def is_disarium(num):
    """
    Function to check if a number is a Disarium number.
    """
    total = 0
    num_str = str(num)
    for i in range(len(num_str)):
        digit = int(num_str[i])
        total += digit ** (i + 1)
    return total == num

# Main Program
number = int(input("Enter a number: "))
if is_disarium(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")
