from sys import argv

script, filename = argv

print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line = "%r \n%r \n%r \n"

print "I'm going to write these to the file."

target.write(line % (line1, line2, line3))
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "Type the filename again:"
file_2 = raw_input(">")
target_2 = open(file_2)
print target_2.read()

print "And finally, we close it."
target_2.close()
