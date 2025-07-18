# Predefined dictionary
data = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore",
    "country": "Pakistan",
    "profession": "Engineer"
}

# Ask the user to enter a key
key = input("Enter the key you want to find the value for: ")

# Check if the key exists in the dictionary
if key in data:
    print(f"The value for key '{key}' is: {data[key]}")
else:
    print(f"Key '{key}' not found in the dictionary.")
