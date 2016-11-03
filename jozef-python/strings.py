# demonstrate how string can be printed

first_number = 4
first_string = "string"

#formaters
print "This is first number: %d" %first_number
print "This is first %s" %first_string
print "This combination of both - number %d and %s" %(first_number, first_string)
print "Jan\nFeb\nMar\n"

#Multiline text
print """
First line of multiline
 Second line of multiline
Third line of multiline

Fifth line of multiline
"""

#print the same string specified number of times
print "*" * 10

#print long string in one line but in code it is in two lines
print "Hello first line",
print "Hello second line."
