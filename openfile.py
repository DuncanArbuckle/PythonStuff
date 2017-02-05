from sys import argv

filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
