#Importing CSV library to read file
import csv

#Returns the Correct Order List
def listSelector (choice):
	if choice == 1:
		return 'meats.csv'
	elif choice == 2:
		return 'ifs.csv'
	elif choice == 3:
		return 'sysco.csv'

#Picks the correct CSV file to open
def selectionMenu ():
	selection = 0
	while selection == 0:
		print ("Welcome to the Order Script, what would you like to place orders for?")
		print ("1)Rocker Bros  2)IFS  3)Sysco")
		selection = int(input('Your Choice? '))
		
		if (selection < 0 or selection > 4):
			selection = 0
			print ("I'm sorry, that's an invalid entry.  Please input again")
		else:
			break
	return selection

#Requests User for quantity they would like to order
def placeOrder(fileName):
	userInputList = []
	with open(fileName) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			print(row[0], row[1])
			quantity = input("How much do you want to order? ")
			#loops and asks again if quantity is empty
			while quantity == "":
				quantity = input("How much do you want to order? ")
			row.append(quantity) #Adds User Requested Quantity into array
			userInputList.append(row)
	
	return userInputList

#Assembles final string for order
def assembleOrder(orderingList):
	orderString = "Hello, I will be placing an order for Chego Tomorrow. For tomorrow we will need... \n"		
	for section in orderingList:
		if(int(section[2]) > 0):
			orderString += section[2] + ' x ' + section[1] + ' ' + section[0] + '\n'

	orderString += "Thanks.  Have a blessed day \n"
	return orderString

#Asks user if they want to palce another order
def askAnotherOrder():
	orderAgain = ''
	while orderAgain == '':
		orderAgain = input ("Would You like to place another order? YES/NO?")
		if orderAgain.lower() == 'yes':
			return 1
		elif orderAgain.lower() == 'no':
			return 0
			break
		else:
			print("I'm sorry.  Invalid Input.")
			orderAgain = ''

#Runs the ordering process while runStatus is 1
def orderEngine(runStatus):			
	while runStatus == 1:
		option = selectionMenu()
		csvFile = listSelector(option)
		orderList = placeOrder(csvFile)
		finalOrder = assembleOrder(orderList)
		
		print (finalOrder)

		runStatus = askAnotherOrder()

orderEngine(1)