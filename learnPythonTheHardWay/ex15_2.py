print "please input a filename:"
filename = raw_input("> ")

txt = open(filename)

print "The content of file %r :" % filename
print txt.read()