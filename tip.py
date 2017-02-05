#This will calculate the script for a 15% and 20% type on a bill

print "\nHere is your handy dandy pocket tip calculator"

bill_total = float(raw_input("What is the total of the bill? "))

tip15 = bill_total * 0.15
tip20 = bill_total * 0.20

whatip = raw_input("What percentage of tip would you like to give? ")
if whatip == '15':
		print "\nThe 15% tip for your bill is: ", tip15
		print "\nThis brings your bill total too: ", bill_total + tip15
elif whatip == '20':
		print "\nThe 20% tip for your bill is: ", tip20
		print "\nThis brings your bill total too: ", bill_total + tip20