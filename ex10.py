tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm\b split\non a line."
backslash_cat = "I'm \ a \ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fini\rshies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

while True:
	for i in ["/","-","|","\\","|"]:
		print "%r\r" % i,