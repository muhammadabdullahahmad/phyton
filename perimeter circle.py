import math

# Function to calculate area and perimeter of a circle
def calculate_circle_properties(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Ask user for the radius
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Radius cannot be negative.")
    else:
        area, perimeter = calculate_circle_properties(radius)
        print(f"\nArea of the circle: {area:.2f}")
        print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")
except ValueError:
    print("Please enter a valid number for radius.")
