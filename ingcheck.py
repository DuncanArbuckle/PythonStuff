##prints out lines of a file that do not match input
ing=raw_input("What ingredients do you have? ")
wordlist = ing.split()
for i in wordlist:
	with open("stuffedchicken.txt") as f:
		found = False
		for line in f:
			if i not in line:
				print(line)
				found = True
		