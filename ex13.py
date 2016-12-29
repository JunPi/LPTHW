from sys import argv

script, first, second, third = argv

# first = raw_input("1st argument: ")
# second = raw_input("2nd argument: ")
# third = raw_input("3rd argument: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# difference for raw_input

one = raw_input("What you think: ")
two = raw_input("What you think more: ")
three = raw_input("What last you think: ")

print "What you have think %r %r %r" % (one, two, three)

