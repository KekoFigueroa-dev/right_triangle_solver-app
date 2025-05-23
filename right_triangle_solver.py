import math # Import required math module for square root function
# Program: Right Triangle Solver App
# Description: This program calculates the hypotenuse and area of a right triangle

#====== Welcome Section ======#
# Display welcome message
print("Welcome to my: Right Triangle Solver App")

#====== Input Section ======#
# Get first leg measurement from user with validation
while True:
    try:
        leg_1 = float(input("What is the first leg of the triangle: "))
        if leg_1 <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Please enter a valid number")
# Get second leg measurement from user with validation
while True:
    try:
        leg_2 = float(input("What is the second leg of the triangle: "))
        if leg_2 <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

#====== Calculation Section ======#
# Calculate hypotenuse using Pythagorean theorem (math.sqrt)
triangle_hypotenuse = math.sqrt((leg_1**2)+(leg_2**2))
# Calculate triangle area
triangle_area = (leg_1 * leg_2)/2
# Round results to 3 decimal places
rounded_hypotenuse = round(triangle_hypotenuse,3)
rounded_area = round(triangle_area,3)

#====== Output Section ======#
# Display hypotenuse and area results
print(f"For a triangle with legs of {round(leg_1,3)} and {round(leg_2,3)} the hypotenuse is {rounded_hypotenuse}.")
print(f"For a triangle with legs of {round(leg_1,3)} and {round(leg_2,3)} the area is {rounded_area}.")

print("Thank you for testing my app! ")