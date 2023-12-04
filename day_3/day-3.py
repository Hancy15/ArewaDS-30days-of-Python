#No 1
age = 23

#No 2
height = 12.4

#No 3
complex_number = 3 + 4j


#No 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle is {area}")



#No 5
# Prompt the user to enter the sides of the triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

# Calculate the perimeter of the triangle
perimeter = side_a + side_b + side_c

# Display the result
print(f"The perimeter of the triangle is {perimeter}")


#No 6
# Prompt the user to enter the length and width of the rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Calculate the area of the rectangle
area = length * width

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + width)

# Display the results
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")


#No 7
# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Define the value of pi
pi = 3.14

# Calculate the area of the circle
area = pi * radius ** 2

# Calculate the circumference of the circle
circumference = 2 * pi * radius

# Display the results
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

#No 8
# Given equation: y = 2x - 2
slope = 2
y_intercept = -2

# Calculate x-intercept (when y = 0)
x_intercept = 0

# Calculate y-intercept (when x = 0)
y_intercept_point = slope * 0 + y_intercept

# Display the results
print(f"Slope: {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept_point}")


#No 9
import math

# Coordinates of the two points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope
slope = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the results
print(f"Slope: {slope}")
print(f"Euclidean Distance: {distance}")


#No 10
import math

# Slope calculation for y = 2x - 2
slope_equation = 2

# Coordinates of the two points for the line passing through (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)

# Compare slopes
if slope_equation == slope_points:
    print("The slopes are equal. The line and the equation are parallel.")
else:
    print("The slopes are not equal. The line and the equation are not parallel.")



#No 11
# Given quadratic equation: y = x^2 + 6x + 9

# Define the quadratic function
def quadratic_function(x):
    return x**2 + 6*x + 9

# Try different x values
for x_value in range(-10, 11):
    y_value = quadratic_function(x_value)
    print(f"For x = {x_value}, y = {y_value}")

    # Check if y is equal to 0
    if y_value == 0:
        print(f"At x = {x_value}, y is equal to 0")



#No 12
#length comparison
string1, string2 = 'python', 'dragon'
falsy_comparison = len(string1) == len(string2)


#No 13
string1, string2 = 'python', 'dragon'
found_in_both = 'on' in string1 and 'on' in string2


#No 14
sentence = "I hope this course is not full of jargon"

# Check if 'jargon' is in the sentence
contains_jargon = 'jargon' in sentence

# Display the result
print(f"Does the sentence contain 'jargon'? {contains_jargon}")


#No 15
string1 = 'python'
string2 = 'dragon'

# Check if 'on' is not in both strings
no_on_in_both = 'on' not in string1 and 'on' not in string2

# Display the result
print(f"There is no 'on' in both 'dragon' and 'python': {no_on_in_both}")

#No 16
text = 'python'

# Find the length of the text
length_of_text = len(text)

# Convert the length to float
length_as_float = float(length_of_text)

# Convert the float to string
length_as_string = str(length_as_float)

# Display the results
print(f"Length of the text 'python': {length_of_text}")
print(f"Length as float: {length_as_float}")
print(f"Length as string: {length_as_string}")


#No 17
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Test the function with some examples
num1 = 6
num2 = 15

print(f"{num1} is even: {is_even(num1)}")
print(f"{num2} is even: {is_even(num2)}")


#No 18
# Floor division of 7 by 3
floor_division_result = 7 // 3

# Integer converted value of 2.7
converted_value = int(2.7)

# Check if the two values are equal
is_equal = floor_division_result == converted_value

# Display the results
print(f"Floor division of 7 by 3: {floor_division_result}")
print(f"Integer converted value of 2.7: {converted_value}")
print(f"Are the two values equal? {is_equal}")



#NO 19
# Check if the type of '10' is equal to the type of 10
are_types_equal = type('10') == type(10)

# Display the result
print(f"Are the types of '10' and 10 equal? {are_types_equal}")


#NO 20
try:
    is_equal_to_10 = int('9.8') == 10
except ValueError:
    is_equal_to_10 = False

# Display the result
print(f"Is int('9.8') equal to 10? {is_equal_to_10}")


#No 21
# Prompt the user to enter hours and rate per hour
hours_worked = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate the weekly earnings
weekly_earnings = hours_worked * rate_per_hour

# Display the result
print(f"Your weekly earning is {weekly_earnings}")


#No 22
# Prompt the user to enter the number of years
years_lived = int(input("Enter number of years you have lived: "))

# Calculate the number of seconds
seconds_lived = years_lived * 365 * 24 * 60 * 60

# Display the result
print(f"You have lived for {seconds_lived} seconds.")


#No 23
# Display the table
print(" 1 1 1 1 1")
print(" 2 1 2 4 8")
print(" 3 1 3 9 27")
print(" 4 1 4 16 64")
print(" 5 1 5 25 125")

