#Importing CSV library to read file
import csv

runStatus = 1 #Keep Looping if 1. Terminate if 0

while runStatus == 1:
	orderList = [] # This will store the arrays for Ordering
	option = 0 # This is the selector for Order Listile
	csvFile = '' #This will be the filename of the selection
	orderAgain = '' #Condition to loop
	
	#Presenting User with Choice
	while option == 0:
		print ("Welcome to the Order Script, what would you like to place orders for?")
		print ("1)Rocker Bros  2)IFS  3)Sysco")
		option = int(input('Your Choice? '))
		
		if (option < 0 or option > 4):
			option = 0
			print ("I'm sorry, that's an invalid entry.  Please input again")
		else:
			break

	#Cases for csvFile
	if option == 1:
		csvFile = 'meats.csv'
	elif option == 2:
		csvFile = 'ifs.csv'
	elif option == 3:
		csvFile = 'sysco.csv'


	#Reading CSV File and loading into Data
	with open(csvFile) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row[0], row[1])
			quantity = input("How much do you want to order? ")
			row.append(quantity) #Adds User Requested Quantity into array
			orderList.append(row)
			
	print ("Hello, I will be placing an order for Chego Tomorrow. For tomorrow we will need...")		
	for section in orderList:
		if(int(section[2]) > 0):
			print(section[2], 'x', section[1], section [0])

	print ("Thanks.  Have a blessed day")

	print ("")
	
	while orderAgain == '':
		orderAgain = input ("Would You like to place another order? YES/NO?")
		if orderAgain.lower() == 'yes':
			runStatus = 1
		elif orderAgain.lower() == 'no':
			runStatus = 0
			break
		else:
			print("I'm sorry.  Invalid Input.")
			orderAgain = ''

		