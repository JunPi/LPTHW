formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") # print out with single quote
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) # 4 times %r as string 
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
) 
# third one print out with double-quotes, other with single quote