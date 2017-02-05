print "opening and closing the file."
text_file = open("sample.txt", "r")
text_file.close()

print "\nReading characters from the file"
text_file = open("sample.txt", "r")
print text_file.read()
text_file.close()
