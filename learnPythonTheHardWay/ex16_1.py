from sys import argv

# unpack the input tuple , assign those to variables
script, filename = argv

# open the file with 'r' mode , meaning you only can use 'read operator' to this file
target = open(filename, 'r')

print target.read()

target.close()