x = "There are %d types of people." % 10 # string format character decimal, define a variable
binary = "binary" # define a variable
do_not = "don't" # define another variable
y = "Those who know %s and those who %s." %(binary, do_not) # string format character string, define a variable


print x # print out
print y # print out
print "I said: %r." % x # string format raw, output field 
print "I also said: %r." % y # string format string


hilarious = False # define a variable
joke_evaluation = "Isn't that joke so funny?! %r" # string format raw

print joke_evaluation % hilarious # both sides are variable

w = "This is the left side of..." # beginning part 
e = "a string with a right side." # last part

print w + e # no space between add two strings directly