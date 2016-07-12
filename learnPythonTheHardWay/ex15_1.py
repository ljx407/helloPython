from sys import argv

script, filename = argv

txt = open(filename)

print "Your filename %r." % filename

print "The content of file %r :" % filename
print txt.read()