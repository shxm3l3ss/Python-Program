import os
from colorama import Fore, Back
from tqdm import tqdm
import time


os.system("cls")

adminslist = ["Dus1610","Andy0211"]

userslist = ["None"]

adminspasswords = ["16102004","02112005"]

passwordslist = []

op = ""

check2 = False 

newUser = False

changelanguage = False


def displayMenu ():

	progress_bar()

	check1 = False

	print("Welcome")
	
	while check1 == False:
		
		op = str(input("\nDo you want to Log in or Register?: "))

		if op.lower() == "log in" or op.lower() == "login":

			login () 

			check1 = True

		elif op.lower() == "register":

			register()

			check1 = True

		else:
			os.system("cls")
			print("\nThats not an option try again")


def register ():

	global username 

	day = 0

	month = 0

	year = 0

	counter = 0

	newUser = True
	
	condition = False

	everything = False

	passw = False

	os.system("cls")

	while condition == False:

		username = str(input("Create your log in username: "))

	
		if username in userslist or username in adminslist:

			os.system("cls")

			print("\nThat username already exists")

			print("\nTry another one\n")

		elif len(username) < 6:

			os.system("cls")

			print("\nUsername must have more that 6 caracters")

			print("\nTry another one\n")

		else:

			condition = True

			userslist.append(username)

			while passw == False:

				password = str(input("\nCreate your log in password: "))

				passwordslist.append(password)

				if len(password) < 6:

					os.system("cls")

					print("\nPassword must have more that 6 caracters")

					print("\nTry another one\n")
				else:
					passw = True


			os.system("cls")

			print("\nGreat so now lets set up your account")

			incorrect = False

			while incorrect == False:

				date = False
				
				months31 = [1,3,5,8,10,12]
				
				months30 = [4,6,8,9,11]

				while date != True:
					day = int(input("\nEnter your birthday (Day): ")) 
					if day <  1 or day > 32:
						print("\nError - incorrect day")
						date = True
					else:
						month = int(input("\nMonth: "))
					if month < 1 or month > 12 and date == False:
						print("Error - incorrect month")
						date = True
					else:
						year = int(input("\nYear: "))

					if year < 1920 or year > 2020 and date == False:
						print("Error - incorrect year")
						date = True
					if year % 4 == 0 and month == 2 and date == False:
						if day <  1 or day > 29:
							os.system("cls")
							print("Incorrect Date\n")
							print("Enter it again")
					elif month < 1 or month > 12 and date == False:
						os.system("cls")
						print("Incorrect Date\n")
						print("Enter it again")	
					elif month == 2 and (day < 1 or day > 28) and date == False:
						os.system("cls")
						print("Incorrect Date\n")
						print("Enter it again")
					elif month == months31 and (day < 1 or day > 31 ) and date == False:
						os.system("cls")
						print( "Incorrect Date\n")
						print("Enter it again")
					elif month == months30 and (day < 1 or day > 30) and date == False:
						os.system("cls")
						print("Incorrect Date\n")
						print("Enter it again")
					elif date == False:
						os.system("cls")
						print("\nNice! We are done now log in\n")
						date = True
						everything = True
						incorrect = True
	
	if everything == True:
		login()

	tutorial()

	

def login ():

	global username

	admin = False
	
	condition = False

	user_normal = False

	check3 = False

	while check3 == False:

		while condition != True:
		
			username = str(input("\nEnter your log in username: "))

			if username in adminslist:

				os.system("cls")

				print("Hi Admin")

				admin = True

				condition = True


			elif username in userslist:

				user_normal = True

				condition = True

			else:
				os.system("cls")
				print("Incorrect username")
				print("\n Lets try again")

		while condition != False:

			while admin == True:

				adminpass = str(input("\nEnter the admin password:"))

				if adminpass in adminspasswords:

					condition = False

					admin = False

					check3 = True

				else:

					os.system("cls")

					print("\nYoure not the admin -_-")

					admin = False

					condition = False


			while user_normal == True:

				password = str(input("\nEnter your password: "))

				if password in passwordslist:
			
					condition = False

					user_normal = False

					check3 = True

					os.system("cls")
		
				else:
					os.system("cls")
					print("Incorrect password")
					print("\n Lets try again")



def tutorial ():

	os.system("cls")

	time.sleep(2)

	print("First you need to know how the menu works so lets complete the tutorial\n")

	time.sleep(3)

	print("User:", username ,"   <---- First here is your username\n")

	time.sleep(3)

	print("Menu options:    <---- Here you have all the menu options \n")

	time.sleep(3)

	print("-Settings     <---- Here are the setings if u want to get in there just type Setings \n")

	time.sleep(3)	

	print("-Log out      <---- Last but not useless log out option to quit your account \n")

	time.sleep(3)

	print("What you want me to do?:       <----Then ill ask you what you want me to do \n")

	time.sleep(3)

	os.system("pause")





def menu ():

	op = "none"

	quit = False

	os.system("cls")

	print("\nUser:",username)

	while quit == False:

		print("\nMenu options:")

		print("\n-Settings")

		print("\n-Log out")

		menuop = str(input("\nWhat you want me to do?: "))

		if menuop.lower() == "settings":

			settings()

		elif menuop.lower() == "log out" or menuop.lower() == "logout":

			os.system("cls")

			quit = True

		else:

			os.system("cls")

			print("\nHuh? Looks like thats not an option")

	

	



def settings ():

	os.system("cls")

	quit = False

	while quit == False:

		print("Settings options:\n")

		print("-Change color\n")

		print("-Quit")

		settingsop = str(input("\nWhat you want to do?: "))

		if settingsop.lower() == "change color" or settingsop.lower() == "changecolor":

			os.system("cls")

			print("This is our color selection: \n \n Blue  \n \n Red  \n \n Green  \n \n Yellow  \n \n White")

			colorop = str(input("\nWhich color is your favorite?: "))

			if colorop.lower() == "blue":

				os.system("cls")

				print( Fore.BLUE + "\nNice we set the color to Blue\n")

			elif colorop.lower() == "red":

				os.system("cls")

				print( Fore.RED + "\nNice we set the color to Red\n")


			elif colorop.lower() == "green":

				os.system("cls")

				print( Fore.GREEN + "\nNice we set the color to Green\n")


			elif colorop.lower() == "yellow":

				os.system("cls")

				print( Fore.YELLOW + "\nNice we set the color to Yellow\n")


			elif colorop.lower() == "white":

				os.system("cls")

				print( Fore.RESET + "\nNice we set the color to White\n")

		elif settingsop.lower() == "quit":

			os.system("cls")

			quit = True
		else:
			print("Huh? Looks like thats not an option")

			print("\n Try again\n")

			os.system("cls")

def progress_bar ():

	os.system("cls")

	print("\n Loading\n")

	for i in tqdm (range(10)) :
		time.sleep(0.5)

	time.sleep(1)

	os.system("cls")

	time.sleep(1)


while check2 == False:

	quit = False
	
	displayMenu()

	menu()

	os.system("cls")

	while quit == False:

		finalop = str(input("Want to quit the program (Yes or No)?: "))


		if finalop.lower() == "yes":

				check2 = True

				quit = True

		elif finalop.lower() == "no":

			print( Fore.RESET + "")

			os.system("cls")

			quit = True

			continue;

		else:

			os.system("cls")

			print("Huh? Looks like thats not an option\n")

	




	
