# import a module named argv that you can use the function below
from sys import argv

# take the parameter that you input in the shell to varaibles
script, filename = argv

# open a file specified by the variable of filename, then assign it to a variable
txt = open(filename)

# print the filename
print "Here's your file %r:" % filename
# read and print the content of file
print txt.read()

txt.close()

# print promt to input the filename again
print "Type the filename again:"
# input a filename from shell and assign it to variable named file_again
file_again = raw_input("> ")

# open a file specified by the variable of file_again
txt_again = open(file_again)

# read and print the file content
print txt_again.read()

txt_again.close()