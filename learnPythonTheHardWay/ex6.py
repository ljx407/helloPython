# define a vaiable named x
x = "Thera are %d types of people." % 10
# define a variable named binary
binary = "binary"
# define a variable named do_not
do_not = "don't"
# define a variable named y
y = "Those who know %s and those who %s." % (binary, do_not)

# print the value of x
print x
# print the value of y
print y

# concate a string with x then print 
print "I said: %r." % x
# concate a string with y then print
print "I alse said: '%s'." % y

# define a variable named hilarous
hilarious = False
# define a variable name joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# print the format variable joke_evaluation
print joke_evaluation % hilarious

# define a variable named w
w = "This is the left side of..."
# define a variable named e
e = "a string with a right side"

# concate w with e then print
print w + e
# python concate two string with space default
print w,e