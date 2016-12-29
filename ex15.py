from sys import argv # import module

script, filename = argv # unpack argument

txt = open(filename) # open the file

print "Here's your file %r:" % filename # display filename
print txt.read() # display content of the file

print "Type the filename again:" # display user input file name
file_again = raw_input(">") # input the file name

txt_again = open(file_again) # open the file 

print txt_again.read() # display content of the file