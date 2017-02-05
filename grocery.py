#Helps decide what meal to make 
import sys 
from itertools import count
from itertools import islice 
from sys import argv 
import difflib

def recipe ( arga, argb ):
	arg2 = arga
	arg3 = argb 
	print "Okay here's what you need for the  %s recipe" % arg3
	if 'Exit' not in open ('%s.txt' % arg2, 'r'):
		with open ('%s.txt' % arg2, 'a') as wf: # opens file for reading as indicated by the r, could also be w for writing
			wf.write('\nExit')
		wf.close()
		with open ('%s.txt' % arg2, 'r') as in_file: 
			num = 0
			for line in in_file: 
				if len(line) == 4:
					print '[25] Exit'
				else: 
					print [num], line
					num += 1
	else:
		with open ('%s.txt' % arg2, 'r') as in_file: 
			num = 0
			for line in in_file: 
				if len(line) == 4:
					print '[25] Exit'
				else: 
					print [num], line
					num += 1
		
def ingrf( args, argb ):	
	arg1 = args
	arg2 = argb 
	with open ('%s.txt' % arg2, 'r') as p:
		lines = p.readlines() # reads all lines from file in a list
		e = str(lines [arg1]) # saving output to a variable 
		print e 
		j = open('ingrhave.txt', 'a') #opens new document for writing 
		for item in e:
			j.write(item) # saves the contents of variable e to a file 
		j.close()
			
def need ( arg ):
	name = arg
	with open('%s.txt' % name , 'r') as file1:
		with open('ingrhave.txt', 'r') as file2:
			same = set(file1).difference(file2)
		same.discard('\n')
		same.discard('Exit')
		print "Here's what you still need:\n " 
		with open('differences.txt', 'w') as file_out:
			for line in same:
				file_out.write(line)
				print line 			
		
meats = ('chicken', 'beef', 'pork');
validans = ('yes', 'no');

loop = True 

while loop == True:
	salemeat = raw_input("Is there any meat on sale? ").lower() #convert all input to lower case
	if salemeat not in validans:
		print "Not a valid response try again"
	while salemeat == 'yes':
		meat = raw_input("Which meat is on sale? ").lower()  #convert all input to lower case
		if meat not in meats:
			print "Not a valid response"
			#meat = raw_input("Which meat is on sale? ").lower() 
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
				recipe ( "stuffedchicken" , 'Stuffed Chicken' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('stuffedchicken.txt'))
				while ingr != 25:
					if ingr > num_lines:
						ingr=input("Please enter a valid response: ")
					#	ingr=input("Which ingredients do you have? (Choose a number): ")
					else:
						ingrf( ingr, "stuffedchicken")
						ingr=input("Which ingredients do you have? (Choose a number): ")
				need ( 'stuffedchicken' )
				sys.exit()
			elif ans == "2":
				recipe ( "butterchicken" , 'Butter Chicken' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('butterchicken.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'butterchicken' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'butterchicken' )
				sys.exit()
			elif ans == "3":
				recipe ( 'chickenparmesan' , 'Chicken Parmesan' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('chickenparmesan.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'chickenparmesan' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'chickenparmesan' )
				sys.exit()
			elif ans == "4":
				recipe ( 'chickenfajitas' , 'Chicken Fajitas' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('chickenfajitas.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'chickenfajitas' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'chickenfajitas' )
				sys.exit()
			elif ans == "5":
				sys.exit()
			else:
				print "Not a valid selection"
		
		while meat == 'beef':
			print ("""
			1. Steak and Brussel Sprouts
			2. Steak Skewers
			3. Rib-Eye Steak with Corn Salad
			4. Steak Fajitas
			5. Exit
			""")
			ans=raw_input("Which dish would you like to make? [Select a number] ")
			if ans == "1":
				recipe ( 'steakandbrussel' , 'Steak and Brussel Sprouts' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('steakandbrussel.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'steakandbrussel' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'steakandbrussel' )
				sys.exit()
			elif ans == "2":
				recipe ( 'steakskewers' , 'Steak Skewers' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('steakskewers.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'steakskewers' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'steakskewers' )
				sys.exit()
			elif ans == "3":
				recipe ( 'steakandsalad' , 'Rib-Eye Steak with Corn Salad' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('steakandsalad.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'steakandsalad' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'steakandsalad' )
				sys.exit()
			elif ans == "4":
				recipe ( 'steakfajitas' , 'Steak Fajitas' )
				ingr=input("Which ingredients do you have? (Choose a number): ")
				o = open('ingrhave.txt', 'w')
				num_lines = sum(1 for line in open('steakfajitas.txt'))
				while ingr != 25 and ingr < num_lines:
					ingrf( ingr, 'steakfajitas' )
					ingr=input("Which ingredients do you have? (Choose a number): ")
				if ingr > num_lines and ingr != 25:
					print "Please enter a valid response"
				else:
					need ( 'steakfajitas' )
				sys.exit()
			elif ans == "5":
				break
			else:
				print "Not a valid selection"
			break
if salemeat == 'no':
	print "\nOkay I'll choose some vegetarian dishes for you."
	veg = raw_input("Which veggies are on sale? ").lower() 
	
	
else:
	print "\nNot a valid response"
	
# Way of checking if entry has more than one response if one responce is desired 
#wordlist = meat.split() #splits the input into a list 
#	wordcount = [] #empty list created 
#	for w in wordlist:
#		wordcount.append(wordlist.count(w)) 
#		adds a 1 to the list for each word counted so two meat items will populate a list as [1, 1]
#	if len(wordcount) > 1:
#		counts the length of the list, if more than one input is given the list will have a length greater than one 
#		print "\nMore than one meat entered"
	
# Diff lab stuff 
#with open("stuffedchicken.txt") as f, open("ingrhave.txt") as g:
			#	flines = f.readlines()
			#	glines = g.readlines()

			#	d = difflib.Differ()
			#	diff = d.compare(flines, glines)
			#	print("\n".join(diff))
	
##do a pause when displaying instructions for making the dish 
## make database/array of ingredients at home then match that against recipe
	
#c = count(meat, 0)
#	print c 
#	if c > 0: 
#		print "\nYou have entered more than one option"

#text_file = open("stuffedchicken.txt", "r") #opens file for reading as indicated by the r, could also be w for writing 
			#print text_file.read() #prints the whole file 

#if meat == "chicken": 
#		print "Which one of these would you like? " 
#		print " ".join([str(x) for x in chickrecipes] ) #prints out all list items