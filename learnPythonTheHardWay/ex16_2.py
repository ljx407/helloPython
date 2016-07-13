from sys import argv

script, filename = argv

target = open(filename, 'w')

# print "The content :",
# print target.read()

raw_input("Are you sure to erase the file?")

print "We are going to erase ,Goodbye!"
target.truncate()

print "I'm going to ask you three lines:"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

line = """
%s
%s
%s
""" % (line1, line2, line3)

# print line

target.write(line)

target.close()
