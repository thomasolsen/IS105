# Formatted variables in the string to print the variables i want.
x = "There are %d types of people." % 10
# a variable
binary = "binary"
# Another variable
do_not = "don't"
# Same as x, formatted variables do get em to print, need () and , to get multiple formats printed.
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the strings so humans can read them.
print x
print y

# Same as over with the formatted variables in the string. 
print "I said %r." % x
print "I also said: '%s'." % y

# boolean value for true or false.
hilarious = False
# Formatted variable in the string.
joke_evaluation = "Isn't that joke so funny?! %r"
# prints the varbiables with the answer false.
print joke_evaluation % hilarious

# Variables ready to print.
w = "This is the left side of..."
e = "a string with a right side."
# Output variables.
print w + e
