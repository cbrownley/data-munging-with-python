#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
from math import *
from string import *
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

# Print a simple string
print "I'm excited to learn Python"

# This line and the next line are comment lines
# Add two numbers together
x = 4
y = 5
z = x + y
print "Four plus five equals %d" % (z)

# This line and the next line are comment lines
# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print a, b, c

# INTEGERS
# x equals 9
x = 9
print x

# 3*3*3*3 = 81
print 3**4

# 8/2 equals 4, then 8.3/2.7 equals approximately 3.074
print int(8.3)/int(2.7)
print 8.3/2.7

# 7/2 equals 3 because of truncation, then 7/2.0 and 7.0/2 both equal 3.5
print 7/2
print 7/2.
print 7./2

# FLOATING-POINT NUMBERS
# 2.5 multiplied by 4.8 equals 12.0
y = 2.5*4.8
print y

# 8/float(3) equals 2.666667
r = 8/float(3)
print r
# 8/3 equals 2 because of truncation
print 8/3

# Show how to format output in print statements
print "%d" % (8.3/2.7)
print '%0.2f' % (8.3/2.7)
s = 8/float(3)
print '%.4f' % (s)

# Some mathematical functions available in the math module
print exp(3)
print log(4)
print sqrt(81)

# STRINGS
# A string with single quotations, therefore include a backslash before
# the single quotation in the contraction "I'm" to print the single quotation
print 'I\'m enjoying learning Python'

# A one-line string, but if the string is long and running off the page on the right
# you can use a "\" to separate the long string into smaller strings on separate lines
print "This is a long string.  Without the backslash it would run off of the page \
on the right in the text editor and be very difficult to read and edit.  By using \
the backslash you can split the long string into smaller strings on separate lines \
so that the whole string is easy to view in the text editor."

# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print '''You can use triple single quotations
for multi-line comment strings'''

# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print """You can also use triple double quotations
for multi-line comment strings"""

# Add two strings together
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print sentence

# Repeat a string four times
print "She is" + " " + "very "*4 + "beautiful."

# Determine the number of characters in a string, including spaces and punctuation
m = len(sentence)
print m

# split()
string1 = "My deliverable is due in May"
string1_list = string1.split()
print string1_list
print string1_list[0]

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print string2_list
print string2_list[5], string2_list[-1]

# join()
new_string = join(string1_list, ' ')
print new_string
print ','.join(string2_list)

# strip()
string3 = "   Remove unwanted characters from this string\t\t    \n"
print "string3:",string3
string3_lstrip = string3.lstrip()
print "lstrip:",string3_lstrip
string3_rstrip = string3.rstrip()
print "rstrip:",string3_rstrip
string3_strip = string3.strip()
print "strip:",string3_strip

string4 = "$$Here's another string that has unwanted characters__---++"
print string4
string4_strip = string4.strip('$_-+')
print string4_strip

# replace()
string3_replace = string3_strip.replace(" ", "!@!")
print string3_replace
string4_replace = string4_strip.replace(" ", ",")
print string4_replace

# lower()
string5 = "Here's WHAT Happens WHEN You Use lower"
print string5.lower()

# upper()
string5 = "Here's what Happens when You Use UPPER"
print string5.upper()

# capitalize()
string5 = "here's WHAT Happens WHEN you use Capitalize"
print string5.capitalize()
string5_list = string5.split()
for word in string5_list:
    print word.capitalize(),

# REGULAR EXPRESSIONS / PATTERN MATCHING
# Count the number of times a pattern appears in a string
print ""
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
regexp = re.compile(r"The", re.I)
count = 0
for word in string_list:
    result = regexp.search(word)
    if result == None:
        pass
    else:
        count += 1
print count

# Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
regexp = re.compile(r"(?P<match_word>The)", re.I)
for word in string_list:
    result = regexp.search(word)
    if result == None:
        pass
    else:
        found = result.group('match_word')
        print found,

# Substitute the letter "a" for the word "the" in the string
print ""
string = "The quick brown fox jumps over the lazy dog."
pattern = r"The"
regexp = re.compile(pattern, re.I)
print regexp.sub("a", string)

# DATES
# Print today's date, as well as the year, month, and day elements
today = date.today()
print 'today: %s' % (today)
print today.year
print today.month
print today.day
current_datetime = datetime.today()
print current_datetime

# Calculate a new date using a timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print 'yesterday: %s' % (yesterday)
eight_hours = timedelta(hours=-8)
print '%s, %s' % (eight_hours.days, eight_hours.seconds)

# Calculate the amount of time between two dates and grab the first element, the number of days
date_diff = today - yesterday
print date_diff
print str(date_diff).split()[0]

# Create a string with a specific format from a date object
print today.strftime('%m/%d/%Y')
print today.strftime('%b %d, %Y')
print today.strftime('%Y-%m-%d')
print today.strftime('%B %d, %Y')

# Create a datetime object with a specific format from a string representing a date
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
print datetime.strptime(date1, '%m/%d/%Y')
print datetime.strptime(date2, '%b %d, %Y')
print datetime.date(datetime.strptime(date3, '%Y-%m-%d')) # include the date portion, not time
print datetime.date(datetime.strptime(date4, '%B %d, %Y')) # include the date portion, not time

# LISTS
# Use square brackets to create a list
# len() counts the number of elements in a list
# max() and min() find the maximum and minimum numbers in numeric lists
# count() counts the number of times a value appears in a list
a_list = [1, 2, 3]
print a_list
print 'a_list has %d elements' % len(a_list)
print 'the maximum value in a_list is %d' % max(a_list)
print 'the minimum value in a_list is %d' % min(a_list)
another_list = ['printer', 5, ['star', 'circle', 9]]
print another_list
print 'another_list also has %d elements' % len(another_list)
print '5 is in another_list %d time' % another_list.count(5)

# Use list indices to access specific values in a list
# [0] is the first value; [-1] is the last value
print a_list[0]
print a_list[1]
print a_list[2]
print a_list[-1]    # to get the last value in a list
print a_list[-2]
print a_list[-3]
print another_list[2]
print another_list[-1]

# Use list slices to access a subset of list values
# Do not include the starting indice to start from the beginning
# Do not include the ending indice to go all of the way to the end
print a_list[0:2]
print another_list[:2]
print a_list[1:3]
print another_list[1:]

# Use [:] to make a copy of a list
a_new_list = a_list[:]    # to copy a list
print a_new_list

# Use + to add two or more lists together
a_longer_list = a_list + another_list    # to add lists together
print a_longer_list

# Use 'in' and 'not in' to check whether specific values are or are not in a list
a = 2 in a_list    # use 'in' to check whether a value is in a list
print a
b = 6 not in a_list    # use 'not in' to check whether a value is not in a list
print b

# Use append() to add additional values to the end of the list
# Use remove() to remove specific values from the list
# Use pop() to remove values from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print a_list
a_list.remove(5)
print a_list
a_list.pop()
a_list.pop()
print a_list

# Use reverse() to reverse a list, in-place, meaning it changes the list
a_list.reverse()
print a_list
a_list.reverse()
print a_list

# Use sort() to sort a list, in-place, meaning it changes the list
# To sort a list without changing the original list, make a copy first
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print unordered_list
list_copy = unordered_list[:]
list_copy.sort()
print list_copy
print unordered_list

# Use sorted() to sort a collection of lists by a position in the lists
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print my_lists_sorted_by_index_3

# Use itemgetter() to sort a collection of lists by two index positions
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], 
       [236,5,5,678], [578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print my_lists_sorted_by_index_3_and_0

# TUPLES
# Use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print my_tuple
print 'my_tuple has %d elements' % len(my_tuple)
print my_tuple[1]
longer_tuple = my_tuple + my_tuple
print longer_tuple

# Unpack tuples with the left-hand side of an assignment operator
one, two, three = my_tuple
print one, two, three
var1 = 'red'
var2 = 'robin'
print var1, var2
# Swap values between variables
var1, var2 = var2, var1
print var1, var2

# Convert tuples to lists and lists to tuples
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print tuple(my_list)
print list(my_tuple)

# DICTIONARIES
# Use curly braces to create a dictionary
# len() counts the number of key-value pairs in a dictionary
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print a_dict
print 'a_dict has %d elements' % len(a_dict)
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print another_dict
print 'another_dict also has %d elements' % len(another_dict)

# Use keys to access specific values in a dictionary
print a_dict['two']
print another_dict['z']

# Use copy() to make a copy of a dictionary
a_new_dict = a_dict.copy()    # to copy a dictionary
print a_new_dict

# Use keys(), values(), and items() to access
# a dictionary's keys, values, and key-value pairs, respectively
print a_dict.keys()
a_dict_keys = a_dict.keys()
print a_dict_keys
print a_dict.values()
print a_dict.items()

# Use has_key(), 'in' / 'not in', or get() to test
# whether a key is in a dictionary
print a_dict.has_key('three')

if 'y' in another_dict.keys(): print 'IN!'
if 'c' not in another_dict.keys(): print 'NOT IN!'

print a_dict.get('three')
print  a_dict.get('four')
print a_dict.get('four', 'Not in dict')

# Use sorted() to sort a dictionary
# To sort a dictionary without changing the original dictionary, make a copy first
print a_dict
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print 'order by keys:', ordered_dict1
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print 'order by values:', ordered_dict2
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print 'order by values, descending:', ordered_dict3
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print 'order by values, ascending:', ordered_dict4

# CONTROL FLOW
# if-else statement
x = 5
if x > 4 or x != 9:
    print x
else:
    print 'x is not greater than 4'

# if-elif-else statement
if x > 6:
    print 'x is greater than six'
elif x > 4 and x == 5:
    print x*x
else:
    print 'x is not greater than 4'
    
# for loop
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
z = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
for number in y:
    print number,
print ""

for i in range(len(z)):
    print i, z[i]

for j in range(len(z)):
    if y[j] > 4:
        print y[j],
print ""

for key, value in another_dict.items():
    print str(key) + " " + str(value)

# compact for loops
# list, set, and dictionary comprehensions
# Select specific rows using a list comprehension
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print rows_to_keep

# Select a set of unique tuples in a list using a set comprehension
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print set_of_tuples1
set_of_tuples2 = set(my_data)
print set_of_tuples2

# Select specific key-value pairs using a dictionary comprehension
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print my_results

# while loop
x = 0
while x < 11:
    print x,
    x += 1
print ""

# FUNCTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return float(sum(numericValues))/len(numericValues) if len(numericValues) > 0 else float('nan')

my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print getMean(my_list)

#import numpy as np
#print np.mean(my_list)

# Calcuate the median of a sequence of numeric values
def getMedian(numericValues):
    theValues = sorted(numericValues)
    if len(theValues) % 2 == 1:
        return theValues[(len(theValues)+1)/2-1]
    else:
        lower = theValues[len(theValues)/2-1]
        upper = theValues[len(theValues)/2]
        return (float(lower + upper))/2

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [4, 6, 8, 10, 12, 14]
#print getMedian(my_list1)
#print getMedian(my_list2)

# EXCEPTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return float(sum(numericValues))/len(numericValues)

my_list1 = [2, 2, 4, 4, 6, 6, 8, 8]
my_list2 = [ ]
# Short version
try:
    print getMean(my_list2)
except ZeroDivisionError as detail:
    print float('nan')
    print "Error:", detail

# Long version
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print float('nan')
    print "Error:", detail
else:
    print "The mean is:", result
finally:
    print "The finally block is executed every time"

# READ A FILE
# Read a single text file
#input_file = sys.argv[1]

#filereader = open(input_file, 'r')
#for row in filereader:
    #print row.strip()
#filereader.close()

#with open(input_file, 'r') as filereader:
#    for row in filereader:
#        print row.strip()

# READ MULTIPLE FILES
# Read multiple text files
#inputPath = sys.argv[1]
#for input_file in glob.glob( os.path.join( inputPath, '*.txt' ) ):
#    filereader = open( input_file, 'r' )
#    for row in filereader:
#        print row.strip()

"""
# WRITE TO A FILE
# Write to a text file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()

# Write to a CSV file
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
"""