# define a string named formatter
formatter = "%r %r %r %r"

#print a string after replace specify value from tuple
print formatter % (1, 2, 3, 4)
#print a string after replace specify value from tuple
print formatter % ("one", "two", "three", "four") 
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	'I had this thing.', 
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
)