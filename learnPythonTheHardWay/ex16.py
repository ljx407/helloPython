# get filename from terminal through argv module
# open the file
# prompt peaple to truncate the file
# truncate file
# get some information from standart input 
# write the stuff to the file
# close the connection to the file

# from the 'sys' package ,import the 'argv' module, so you can use the function/methods of 'argv'
from sys import argv

# get the value that inputed from the shell , then assign those to the variables
script, filename = argv

# print the file we will erase, prompt people if or not erase it, 'yes' hit RETURN 'NOT' hit "CTRL+C"
print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^c)."
print "If you want that , hit RETURN."

# wait the decision, erase or not ?
raw_input("?")

# open the file specifed by user
print "Opening the file..."
# if you specify 'w' mode , meaning you can only use "write operator"
target = open(filename, 'w')

# print "The content :",
# print target.read()

# erase the content of the file
# actually when you open the file with 'w' mode , python will erase the file first, so the truncate function here is meaningless
print "Truncating the file. Goodbye!"
target.truncate()

# get three lines that user input from shell
print "How I'm going to ask you for three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

# write all the stuff user input to the file
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close the connection
print "And finally, wo close it."
target.close()