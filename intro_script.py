#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
from string import *
from datetime import date, datetime
import sys
import glob
import os

# Lines that start with a hash/pound sign are one-line comments

# Print a simple string with the print command
print "Output #1: I'm excited to learn Python"

# **************** SECTION 1: NUMBERS ****************  

# Add two numbers together
x = 4
y = 5
z = x + y
# Print the value of z, which is the sum of x and y
# The str() function converts anything into a string
print "Output #2: Four plus five equals " + str(z)

# 7/2 equals 3 because of integer truncation
# 7/2.0 and 7.0/2 both equal 3.5 because at least one number is floating-point
print "Output #3: " + str(7/2)
print "Output #4: " + str(7/2.0)
print "Output #5: " + str(7.0/2)

# **************** SECTION 2: STRINGS ****************  

# Add two strings together
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print "Output #6:" + sentence

# String manipulation
string = "   Remove unwanted characters from this string\t\t    \n"

# strip(): Remove unwanted characters from both ends of a string
print "Output #7: string=" + string
string_strip = string.strip()
print "Output #8: stripped string=" + string_strip

# replace(): Replace one character in a string with another character
string_replace = string_strip.replace(" ", ",")
print "Output #9: " + string_replace

# **************** SECTION 3: DATES ****************  

# Print today's date, as well as the year, month, and day elements
today = date.today()
print "Output #10: " + str(today)
print "Output #11: " + str(today.year)
print "Output #12: " + str(today.month)
print "Output #13: " + str(today.day)
current_datetime = datetime.today()
print "Output #14: " + str(current_datetime)

# Create a string from a date object, with a specific format
print "Output #15: " + str(today.strftime('%m/%d/%Y'))
print "Output #16: " + str(today.strftime('%Y-%m-%d'))

# Create a datetime object and a date object from strings representing dates, with specific formats
date1 = today.strftime('%m/%d/%Y')
print "Output #17: " + str(datetime.strptime(date1, '%m/%d/%Y'))
date2 = today.strftime('%Y-%m-%d')
print "Output #18: " + str(datetime.date(datetime.strptime(date2, '%Y-%m-%d'))) # include the date portion, not time

# **************** SECTION 4: LISTS ****************  

# Use square brackets to create a list
a_list = [1, 2, 3]
print "Output #19: " + str(a_list)
print "Output #20: a_list has " + str(len(a_list)) + " elements" 

# Use list indices / index values to access specific values in a list
print "Output #21: " + str(a_list[0])
print "Output #22: " + str(a_list[1])
print "Output #23: " + str(a_list[2])

# Strings and lists
string = "Your,deliverable,is,due,in,June"

# split(): Split a string into a list based on a specific character
string_list = string.split(',')
print "Output #24: " + str(string_list)

# join(): Join list elements into a string with a specific delimiter
new_string = join(string_list, ' ')
print "Output #25: "+ new_string
print "Output #26: " + '\t'.join(string_list)

# Use 'in' and 'not in' to check whether specific values are or are not in a list
number1 = 2
if number1 in a_list:
	print "Output #27: " + str(number1) + " is in the list"

number2 = 5
if number2 not in a_list:
	print "Output #28: " + str(number2) + " is not in the list"
	
# Or use an if-else statement
number3 = 10
if number3 in a_list:
	print "Output #29: " + str(number3) + " is in the list"
else:
	print "Output #29: " + str(number3) + " is not in the list"
		
# Use append() to add additional values to the end of the list
a_list.append(4)
a_list.append(5)
print "Output #30: " + str(a_list)
print "Output #31: a_list has " + str(len(a_list)) + " elements"

# **************** SECTION 5: DICTIONARIES ****************  

# Use curly braces to create a dictionary
a_dict = {'one':1, 'two':2, 'three':3}
print "Output #32: " + str(a_dict)
print "Output #33: a_dict has " + str(len(a_dict)) + " elements"

# Use has_key(), 'in' / 'not in', or get() to test whether a key is in a dictionary
if 'c' not in a_dict.keys():
	print "Output #34: c is NOT IN the keys of the dictionary so add it with the value 4!"
	a_dict['c'] = 4

# **************** SECTION 6: CONTROL FLOW ****************  

# looping through elements in a list to print the elements
z_list = [99, 88, 77, 66, 55, 44, 33, 22, 11]
print "Output #35:",
for number in z_list:
    print number,
print ""

# looping through the index values of a list to print the elements 
print "Output #36: "
for index_value in range(len(z_list)):
    print index_value, z_list[index_value]

# nested control statements
print "Output #37: "
for number in z_list:
	if number > 44 and number <= 77:
		print str(number) + " is greater than 44 and less than or equal to 77"
	else:
		print str(number) + " is less than or equal to 44 or greater than 77"

# **************** SECTION 7: READING AND WRITING TO FILES ****************  

# Read a single text file
input_file = "letters.txt"
#input_file = sys.argv[1]

print "Output #38: "
with open(input_file, 'r') as filereader:
    for row in filereader:
        print row.strip()

# Read multiple text files
input_path = "."

print "Output #39: "
for input_file in glob.glob(os.path.join(input_path,'*.txt')):
    filereader = open(input_file, 'r')
    for row in filereader:
        print row.strip()

# Write to a CSV file
my_list = [65, 'tiger', 32.05, 'facebook', 41, 'happy new year', 3.14159, '2*pi*r']
max_index = len(my_list)
output_file = "output.csv"
filewriter = open(output_file, 'w')
for index_value in range(len(my_list)):
    if index_value < (max_index-1):
        filewriter.write(str(my_list[index_value])+',')
    else:
        filewriter.write(str(my_list[index_value])+'\n')
filewriter.close()
print "Output #40: Output written to file " + str(output_file)