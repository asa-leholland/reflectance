
# Import regex (regular expressions) package to handle regex searches
import re


# Text file with our metadata
test = '''RADIANCE_ADD_BAND_10 = 0.10000
    RADIANCE_ADD_BAND_11 = 0.10000
    REFLECTANCE_MULT_BAND_1 = 2.0000E-05
    REFLECTANCE_MULT_BAND_2 = 2.0000E-05
    REFLECTANCE_MULT_BAND_3 = 2.0000E-05
    REFLECTANCE_MULT_BAND_4 = 2.0000E-05
    REFLECTANCE_MULT_BAND_5 = 2.0000E-05
    REFLECTANCE_MULT_BAND_6 = 2.0000E-05
    REFLECTANCE_MULT_BAND_7 = 2.0000E-05
    REFLECTANCE_MULT_BAND_8 = 2.0000E-05
    REFLECTANCE_MULT_BAND_9 = 2.0000E-05
    REFLECTANCE_ADD_BAND_1 = -0.100000
    REFLECTANCE_ADD_BAND_2 = -0.100000
    REFLECTANCE_ADD_BAND_3 = -0.100000
    REFLECTANCE_ADD_BAND_4 = -0.100000
    REFLECTANCE_ADD_BAND_5 = -0.100000
    REFLECTANCE_ADD_BAND_6 = -0.100000
    REFLECTANCE_ADD_BAND_7 = -0.100000
    REFLECTANCE_ADD_BAND_8 = -0.100000
    REFLECTANCE_ADD_BAND_9 = -0.100000'''

# Set up our regex pattern to match the Reflectance values
pattern = '([-]?[0-9]+.[0-9]+[E]?[-]?[0-9]*)'


# Iterate over the numbers of the intgers we want to save
for x in range(1,10):

	# For each number, convert the integer to a string
	number = str(x)

	# The regex search follows this format:
	# r1 = re.findall(pattern we are searching for, string we are searching)

	# This search is built to look for the base string + the provided number + the pattern to match our reflectance values
	r1 = re.findall(f'REFLECTANCE_MULT_BAND_{number} = {pattern}', test)

	# print the output (an array of all matching values)
	print(r1)

# Side example about how to use f-strings 
value = 'cat'
other = 'dog'

# Regular statment
print(value + ' is a ' + other)

# Same statement as an 
print(f'{value} is a {other}')
print(value + ' is a ' + other)




# Setup to add at the beginning:
# input statement prompts user for information, then can be used to save it as a variable

# Prompt user for date
date = input('What is the date? Ex: "10_19_20". ')
print(f'The date is {date}.')

# Prompt user for description
desc = input('What is the description? Ex: "sonoma". ')
print(f'The description is {desc}.')