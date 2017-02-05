import sys 
from itertools import count
from itertools import islice 
from sys import argv 
import difflib
meats = ('chicken', 'beef', 'pork');

def recipe ( args ):
	arg2 = args 
	print "Okay here's what you need for the  Stuffed Chicken recipe"
	with open ('%s.txt' % arg2, 'r') as in_file: # opens file for reading as indicated by the r, could also be w for writing
		num = 0
		for line in in_file: 
			print [num], line
			num += 1
			
def ingrf( args ):	
	arg1 = args
	o = open('ingrhave.txt', 'w')
	while arg1 != 100: 
		with open ('stuffedchicken.txt', 'r') as p:
			lines = p.readlines() # reads all lines from file in a list
			e = str(lines [arg1]) # saving output to a variable 
			print e 
		j = open('ingrhave.txt', 'a') #opens new document for writing 
		for item in e:
			j.write(item) # saves the contents of variable e to a file 
		j.close()
		ingr=input("Which ingredients do you have? (Choose a number): ")
		with open('stuffedchicken.txt', 'r') as file1:
			with open('ingrhave.txt', 'r') as file2:
				same = set(file1).difference(file2) # checks two files for any differences 
		same.discard('\n')
		print "Here's what you still need:\n " 
		with open('differences.txt', 'w') as file_out:
			for line in same:
				file_out.write(line) #writes differences to a file 
				print line # prints each line of the file content
				return 

		

salemeat = raw_input("Is there any meat on sale? ").lower() #convert all input to lower case
if salemeat == 'yes':
	meat = raw_input("Which meat is on sale? ").lower()  #convert all input to lower case
	if meat not in meats:
		print "Not a valid response"
	while meat == 'chicken': 
		print ("""
		1. Stuffed Chicken
		2. Butter Chicken
		3. Chicken Parmesan
		4. Chicken Fajitas
		5. Exit
		""")
		
		ans=raw_input("Which dish would you like to make [Select Number]? ")
		if ans == "1":
			recipe ( "stuffedchicken" )
			ingr=input("Which ingredients do you have? (Choose a number): ")
			while ingr != 100:
				ingrf ( ingr )
			break
	#break		
		elif ans == "2":
			recipe ( "butterchicken" )
			ingr=input("Which ingredients do you have? (Choose a number): ")
			o = open('ingrhave.txt', 'w')
			while ingr != 100:
				ingrf( ingr )
				ingr=input("Which ingredients do you have? (Choose a number): ")
			with open('butterchicken.txt', 'r') as file1:
				with open('ingrhave.txt', 'r') as file2:
					same = set(file1).difference(file2)
			same.discard('\n')
			print "Here's what you still need:\n " 
			with open('differences.txt', 'w') as file_out:
				for line in same:
					file_out.write(line)
					print line 
			break 
		elif ans == "3":
			recipe ( "chickenparmesan" )
			ingr=input("Which ingredients do you have? (Choose a number): ")
			o = open('ingrhave.txt', 'w')
			while ingr != 100:
				ingrf( ingr )
				ingr=input("Which ingredients do you have? (Choose a number): ")
			with open('chickenparmesan.txt', 'r') as file1:
				with open('ingrhave.txt', 'r') as file2:
					same = set(file1).difference(file2)
			same.discard('\n')
			print "Here's what you still need:\n " 
			with open('differences.txt', 'w') as file_out:
				for line in same:
					file_out.write(line)
					print line 
			break
		elif ans == "4":
			recipe ( "chickenfajitas" )
			ingr=input("Which ingredients do you have? (Choose a number): ")
			o = open('ingrhave.txt', 'w')
			while ingr != 100:
				ingrf( ingr )
				ingr=input("Which ingredients do you have? (Choose a number): ")
			with open('chickenfajitas.txt', 'r') as file1:
				with open('ingrhave.txt', 'r') as file2:
					same = set(file1).difference(file2)
			same.discard('\n')
			print "Here's what you still need:\n " 
			with open('differences.txt', 'w') as file_out:
				for line in same:
					file_out.write(line)
					print line 
			break		
		elif ans == "5":
			break
		else:
			print ("Not a valid selection")
			#break
elif salemeat == 'no':
	print "Okay here's some vege options"
else:
	salemeat = raw_input("Not a proper response, please enter again: ").lower()