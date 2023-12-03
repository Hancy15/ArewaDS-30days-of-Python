# 'Day 2: 30 Days of python programming'


# Exercise 1

first_Name = 'Sadiq'
last_Name = 'Aliyu'
full_Name = 'Sadiq Muhammad Aliyu'
country = 'Nigeria'
city = 'Kano'
age = 28
year = 2023
is_Married = True
is_true = True
is_Light_On = True


first_Name, last_Name, full_Name, country,city, age,year, is_Married, is_true, is_Light_On = 'Sadiq', 'Aliyu','Sadiq Muhammad Aliyu', 'Nigeria', 'Kano', 28, 2023, True, True,True

# Exercise 2

#1
print(type(first_Name))
print(type(last_Name))
print(type(full_Name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_Married))
print(type(is_true))
print(type(is_Light_On))


#2
print(len(first_Name))

#3
# Compare the length of the first name and last name
if len(first_Name) > len(last_Name):
    print(f"{first_Name} has a longer length than {last_Name}.")
elif len(first_Name) < len(last_Name):
    print(f"{last_Name} has a longer length than {first_Name}.")
else:
    print(f"{first_Name} and {last_Name} have the same length.")

#4
num_one = 5
num_two = 4
#1
total = num_one + num_two
#2
diff = num_one - num_two
#3
product = num_one * num_two
#4
division = num_one / num_two
#5
remainder = num_one % num_two
#6
exp = num_one ** num_two
#7
floor_division = num_one // num_two



#5 The radius of a circle is 30 meters.

import math

radius = 30
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius

# Print the results
print(f"The area of the circle is: {area_of_circle} square meters.")
print(f"The circumference of the circle is: {circum_of_circle} meters.")

# Take user input for radius
user_radius = float(input("Enter the radius of the circle: "))

# Calculate the area based on user input
user_area_of_circle = math.pi * user_radius**2

# Print the result for user-provided radius
print(f"The area of the circle with radius {user_radius} is: {user_area_of_circle} square meters.")



#6
# Get user input for first name
first_name = input("Enter your first name: ")

# Get user input for last name
last_name = input("Enter your last name: ")

# Get user input for country
country = input("Enter your country: ")

# Get user input for age
age = input("Enter your age: ")

# Display the collected information
print("\nUser Information:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

