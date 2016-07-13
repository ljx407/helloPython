from sys import argv

script, user_name, gender = argv
# prompt = "> "
prompt = "==>"

print "Hi %s, I'm the %s script." % (gender,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
living = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about likeing me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, living, computer)