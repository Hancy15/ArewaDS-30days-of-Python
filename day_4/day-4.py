# %% [markdown]
# Exercises - Day 4

# %% [markdown]
# No. 1
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

# %%
result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(result)


# %% [markdown]
# No. 2
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

# %%
result = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(result)


# %% [markdown]
# No. 3
# Declare a variable named company and assign it to an initial value "Coding For All".

# %%
company = "Coding For All"


# %% [markdown]
# No. 4
# Print the variable company using print().

# %%
print(company)

# %% [markdown]
# No. 5 Print the length of the company string using len() method and print().

# %%
company = "Coding For All"
length_of_company = len(company)

print("Length of the company string:", length_of_company)


# %% [markdown]
# No. 6 Change all the characters to uppercase letters using upper() method.

# %%
company = "Coding For All"
uppercase_company = company.upper()

print("Uppercase version of the company string:", uppercase_company)


# %% [markdown]
# No. 7 Change all the characters to lowercase letters using lower() method.

# %%
company = "Coding For All"
lowercase_company = company.lower()

print("Lowercase version of the company string:", lowercase_company)


# %% [markdown]
# No. 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

# %%
company = "Coding For All"

# Capitalize the first letter of the string
capitalized_company = company.capitalize()
print("Capitalized version:", capitalized_company)

# Convert the first letter of each word to uppercase
title_company = company.title()
print("Titlecased version:", title_company)

# Swap the case of each character in the string
swapcase_company = company.swapcase()
print("Swapped case version:", swapcase_company)


# %% [markdown]
# No. 9 Cut(slice) out the first word of Coding For All string.

# %%
company = "Coding For All"
first_word = company.split()[0]

print("First word:", first_word)


# %% [markdown]
# No. 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.

# %%
company = "Coding For All"
index_of_coding = company.find("Coding")

if index_of_coding != -1:
    print("The word 'Coding' is present at index:", index_of_coding)
else:
    print("The word 'Coding' is not present in the string.")


# %% [markdown]
# No. 11 Replace the word coding in the string 'Coding For All' to Python.

# %%
company = "Coding For All"
updated_company = company.replace("Coding", "Python")

print("Updated string:", updated_company)


# %% [markdown]
# No. 12 Change Python for Everyone to Python for All using the replace method or other methods.

# %%
original_text = "Python for Everyone"
updated_text = original_text.replace("Everyone", "All")

print("Updated text:", updated_text)


# %% [markdown]
# No. 13 Split the string 'Coding For All' using space as the separator (split()) 

# %%
company = "Coding For All"
word_list = company.split()

print("List of words:", word_list)


# %% [markdown]
# No. 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

# %%
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(', ')

print("List of companies:", company_list)


# %% [markdown]
# No. 15 What is the character at index 0 in the string Coding For All.

# %%
company = "Coding For All"
character_at_index_0 = company[0]

print("Character at index 0:", character_at_index_0)


# %% [markdown]
# No. 16 What is the last index of the string Coding For All.

# %%
company = "Coding For All"
last_character = company[-1]

print("Last character at index -1:", last_character)


# %% [markdown]
# No. 17 What character is at index 10 in "Coding For All" string.

# %%
company = "Coding For All"
character_at_index_10 = company[10]

print("Character at index 10:", character_at_index_10)


# %% [markdown]
# No. 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.

# %%
name = "Python For Everyone"
acronym = "".join(word[0] for word in name.split())
print("Acronym:", acronym)


# %% [markdown]
# No. 19 Create an acronym or an abbreviation for the name 'Coding For All'.

# %%
name = "Coding For All"
acronym = "".join(word[0] for word in name.split())
print("Acronym:", acronym)


# %% [markdown]
# No. 20 Use index to determine the position of the first occurrence of C in Coding For All.

# %%
text = "Coding For All"
position_of_C = text.index('C')

print("Position of the first occurrence of 'C':", position_of_C)


# %% [markdown]
# No. 21 Use index to determine the position of the first occurrence of F in Coding For All.

# %%
text = "Coding For All"
position_of_F = text.index('F')

print("Position of the first occurrence of 'F':", position_of_F)


# %% [markdown]
# No. 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

# %%
text = "Coding For All People"
position_of_last_l = text.rfind('l')

print("Position of the last occurrence of 'l':", position_of_last_l)


# %% [markdown]
# No. 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_because = sentence.index('because')

print("Position of the first occurrence of 'because':", position_of_because)


# %% [markdown]
# No. 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_last_because = sentence.rindex('because')

print("Position of the last occurrence of 'because':", position_of_last_because)


# %% [markdown]
# No. 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[29:54]

print("Extracted phrase:", phrase)


# %% [markdown]
# No. 26 ind the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
position_of_because = sentence.find('because')

print("Position of the first occurrence of 'because':", position_of_because)


# %% [markdown]
# No. 27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# %%
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[30:54]

print("Sliced phrase:", phrase)


# %% [markdown]
# No. 28 Does ''Coding For All' start with a substring Coding? 

# %%
text = 'Coding For All'
starts_with_coding = text.startswith('Coding')

if starts_with_coding:
    print("The string starts with 'Coding'")
else:
    print("The string does not start with 'Coding'")


# %% [markdown]
# No. 29 Does 'Coding For All' end with a substring coding?

# %%
text = 'Coding For All'
ends_with_coding = text.lower().endswith('coding')

if ends_with_coding:
    print("The string ends with 'coding'")
else:
    print("The string does not end with 'coding'")


# %% [markdown]
# No. 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.

# %%
text = '   Coding For All      '
trimmed_text = text.strip()

print("Trimmed string:", trimmed_text)


# %% [markdown]
# No. 31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

# %%
# Variables
variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"

# Check if they are valid identifiers
result1 = variable1.isidentifier()
result2 = variable2.isidentifier()

# Output the results
print(f"Is '{variable1}' a valid identifier? {result1}")
print(f"Is '{variable2}' a valid identifier? {result2}")

# the variables that will show True when we used the isidentifier() method
#Is '30DaysOfPython' a valid identifier? False
#Is 'thirty_days_of_python' a valid identifier? True



# %% [markdown]
# No. 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

# %%
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)

print("Joined string:", joined_libraries)


# %% [markdown]
# No. 33 Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

# %%
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."

combined_text = sentence1 + '\n' + sentence2

print(combined_text)


# %% [markdown]
# No. 34 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

# %%
header = "Name\tAge\tCountry\tCity"
data = "Asabeneh\t250\tFinland\tHelsinki"

print(header)
print(data)


# %% [markdown]
# No. 35 Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

# %%
radius = 10
area = 3.14 * radius ** 2

result = "The area of a circle with radius {} is {} square meters.".format(radius, area)

print(result)


# %% [markdown]
# No. 36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

# %%
num1 = 8
num2 = 6

addition_result = "{} + {} = {}".format(num1, num2, num1 + num2)
subtraction_result = "{} - {} = {}".format(num1, num2, num1 - num2)
multiplication_result = "{} * {} = {}".format(num1, num2, num1 * num2)
division_result = "{} / {} = {:.2f}".format(num1, num2, num1 / num2)
modulo_result = "{} % {} = {}".format(num1, num2, num1 % num2)
floor_division_result = "{} // {} = {}".format(num1, num2, num1 // num2)
exponential_result = "{} ** {} = {}".format(num1, num2, num1 ** num2)

print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(division_result)
print(modulo_result)
print(floor_division_result)
print(exponential_result)



