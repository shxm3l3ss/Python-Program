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


def displayMenu_ENG ():

	global quit

	global changelanguage

	global language

	global turnoffop 

	progress_bar_ENG()

	check1 = False
	
	while check1 == False:

		print("Welcome")

		print("\n -Register")

		print("\n -Log in")

		print("\n -Change language")
		
		op = str(input("\nWhat you want to do?: "))

		if op.lower() == "log in" or op.lower() == "login":

			login_ENG () 

			check1 = True

		elif op.lower() == "register":

			register_ENG()

			check1 = True

		elif op.lower() == "change language" or op.lower() == "changelanguage":

			go_out = False

			os.system("cls")

			print("You get in the language option\n")

			while go_out == False:

				print("languages list:")

				print("\nEnglish")

				print("\nSpanish")

				languageop = str(input("\nSo what language you want to use?: "))

				if languageop.lower() == "english":

					os.system("cls")

					print("It is already the current language\n")

					go_out = True

				elif languageop.lower() == "spanish":

					language = "SPA"

					os.system("cls")

					print("Estamos haciendo algunos cambios para pasar a Español por favor espere")

					time.sleep(3)

					check1 = True

					changelanguage = True

					quit = True

					go_out = True

					turnoffop = False

				else:

					os.system("cls")

					print("Thats not an option")

					print("\nTry again\n")

		else:
			os.system("cls")
			print("\nThats not an option try again")

def displayMenu_SPA ():

	global language

	global quit 

	global SPA_ENG

	global turnoffop

	quit = False

	progress_bar_SPA()

	check1 = False
	
	while check1 == False:
		
		print("Bienvenido")

		print("\n -Registrarse")

		print("\n -Iniciar Sesion")

		print("\n -Cambiar idioma")
		
		op = str(input("\nQue quieres hacer?: "))


		if op.lower() == "iniciar sesion" or op.lower() == "iniciarsesion":

			login_SPA () 

			check1 = True

		elif op.lower() == "registrarte":

			register_SPA()

			check1 = True

		elif op.lower() == "cambiar idioma" or op.lower() == "cambiaridioma":

			os.system("cls")

			print("Estas en la opcion de cambiar idioma")

			go_out = False

			while go_out == False:

				print("\nlista de idimas:")

				print("\nIngles (English)")

				print("\nEspañol (Spanish)")

				languageop = str(input("\nQue lenguaje quieres usar?: "))

				if languageop.lower() == "ingles" or languageop.lower() == "english":

					language = "ENG"

					os.system("cls")

					print("please wait while we set up everything to English")

					time.sleep(3)

					check1 = True

					changelanguage = False

					go_out = True

					turnoffop = False

					SPA_ENG = True

				elif languageop.lower() == "español" or languageop.lower() == "spanish":

					os.system("cls")

					print("Es tu idioma atual\n")


					go_out = True

				else:

					os.system("cls")

					print("Esa no es una opcion")

					print("\nIntenta otra vez")

		else:
			os.system("cls")

			print("Esa no es una opcion\n")


def register_ENG ():

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
		login_ENG()

	tutorial_ENG()

def register_SPA ():

	global language

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

	if language == "SPA":

		os.system("cls")

		while condition == False:

			username = str(input("Crea tu nombre de usuario: "))

	
			if username in userslist or username in adminslist:

				os.system("cls")

				print("\nEse nombre de usuario ya existe")

				print("\nPrueba otro\n")

			elif len(username) < 6:

				os.system("cls")

				print("\nEl nombre de usuario debe tener mas de 6 caracteres")

				print("\nPrueba otro\n")

			else:

				condition = True

				userslist.append(username)

				while passw == False:

					password = str(input("\nCrea tu contraseña: "))

					passwordslist.append(password)

					if len(password) < 6:

						os.system("cls")

						print("\nLa contraseña debe tener mas de 6 caracteres")

						print("\nPrueba otro\n")
					else:
						passw = True


				os.system("cls")

				print("\nGenia! Ahora vamos a configurar tu cuenta")

				incorrect = False

				while incorrect == False:

					date = False
				
					months31 = [1,3,5,8,10,12]
				
					months30 = [4,6,8,9,11]

					while date != True:
						day = int(input("\nIngresa tu fecha de nacimiento (Dia): ")) 
						if day <  1 or day > 32:
							print("\nError - dia incorrecto")
							date = True
						else:
							month = int(input("\nMonth: "))
						if month < 1 or month > 12 and date == False:
							print("Error - mes incorrecto")
							date = True
						else:
							year = int(input("\nYear: "))

						if year < 1920 or year > 2020 and date == False:
							print("Error - año incorrecto")
							date = True
						if year % 4 == 0 and month == 2 and date == False:
							if day <  1 or day > 29:
								os.system("cls")
								print("Fecha incorrecta\n")
								print("Ingresala otra vez")
						elif month < 1 or month > 12 and date == False:
							os.system("cls")
							print("Fecha incorrecta\n")
							print("Ingresala otra vez")	
						elif month == 2 and (day < 1 or day > 28) and date == False:
							os.system("cls")
							print("Fecha incorrecta\n")
							print("Ingresala otra vez")
						elif month == months31 and (day < 1 or day > 31 ) and date == False:
							os.system("cls")
							print( "Fecha incorrecta\n")
							print("Ingresala otra vez")
						elif month == months30 and (day < 1 or day > 30) and date == False:
							os.system("cls")
							print("Fecha incorrecta\n")
							print("Ingresala otra vez")
						elif date == False:
							os.system("cls")
							print("\nListo! Ahora solo inicia sesion\n")
							date = True
							everything = True
							incorrect = True
	
		if everything == True:
			login_SPA()

		tutorial_SPA()

def login_ENG ():

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

def login_SPA ():

	global language

	global username

	admin = False
	
	condition = False

	user_normal = False

	check3 = False

	if language == "SPA":

		while check3 == False:

			while condition != True:
		
				username = str(input("\nIngresa tu nombre de usuario: "))

				if username in adminslist:

					os.system("cls")

					print("Hola Admin")

					admin = True

					condition = True


				elif username in userslist:

					user_normal = True

					condition = True

				else:
					os.system("cls")
					print("Nombre de usuario incorrecto")
					print("\n Intentemos otra vez")

			while condition != False:

				while admin == True:

					adminpass = str(input("\nIngresa la cotraseña de admin:"))

					if adminpass in adminspasswords:

						condition = False

						admin = False

						check3 = True

					else:

						os.system("cls")

						print("\nTu no eres el admin -_-")

						admin = False

						condition = False


				while user_normal == True:

					password = str(input("\nIngresa tu contraseña: "))

					if password in passwordslist:
			
						condition = False

						user_normal = False

						check3 = True

						os.system("cls")
		
					else:
						os.system("cls")
						print("Contraseña incorrecta")
						print("\n Intentemos otra vez")


def tutorial_ENG ():

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

def tutorial_SPA ():

	os.system("cls")

	time.sleep(2)

	print("Primero necesitas saber como funciona el menu\n")

	time.sleep(3)

	print("Usuario:", username ,"   <---- Primero aqui esta tu nombre de usuario\n")

	time.sleep(3)

	print("Menu de opciones:    <---- Aqui tienes todas las opciones del menu \n")

	time.sleep(3)

	print("-Configuraciones     <---- Aqui tienes las configuraciones solo escribe configuraciones para entrar \n")

	time.sleep(3)	

	print("-Cerrar Sesion      <---- Por ultimo pero no menos importante Cerrar Sesion para salir de tu cuenta \n")

	time.sleep(3)

	print("Que quieres que haga?:       <----Luego te pregutare que quieres que haga \n")

	time.sleep(3)

	os.system("pause")

def settings_ENG ():

	global changelanguage

	global language

	global quit

	global afterchange_SPA

	global turnoffop

	os.system("cls")

	quit = False

	while quit == False:

		go_out = False

		if language == "ENG":

			print("Settings options:\n")

			print("-Change color\n")

			print("-Change language\n")

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

			elif settingsop.lower() == "change language" or settingsop.lower() == "changelanguage":

				os.system("cls")

				while go_out == False:

					print("languages list:")

					print("\nEnglish")

					print("\nSpanish")

					print("\nQuit")

					languageop = str(input("\nSo what language you want to use?: "))

					if languageop.lower() == "english":

						language = "ENG"

						go_out = True

						os.system("cls")

						print("It is already the current language")

					elif languageop.lower() == "spanish":

						changelanguage = True

						os.system("cls")

						print("I need to restart before i can display",languageop,"language")

						op = str(input("\nis it ok? (Yes or No): "))

						if op.lower() == "yes":

							language = "SPA"

							quit = True

							turnoffop = False

						elif op.lower() == "no":

							os.system("cls")

							print("Okay we will not restart") 

							time.sleep(3)

							os.system("cls")

							language = "ENG"

							afterchange_SPA = True

						go_out = True

					elif languageop.lower() == "quit":

						go_out = True

						os.system("cls")


					else:

						os.system("cls")

						print("Thats not an option")

						print("\nTry again\n")

			elif settingsop.lower() == "quit":

				os.system("cls")

				quit = True
			else:
				print("Huh? Looks like thats not an option")

				print("\n Try again\n")

				os.system("cls")

def settings_SPA ():

	global SPA_ENG

	global changelanguage

	global language

	global afterchange_ENG

	global turnoffop

	os.system("cls")

	quit = False

	while quit == False:

		go_out = False

		if language == "SPA":

			print("Opciones de configuracion:\n")

			print(" -Cambiar color\n")

			print(" -Cambiar idioma\n")

			print(" -Salir")

			settingsop = str(input("\nQue quieres que haga?: "))

			if settingsop.lower() == "cambiar color" or settingsop.lower() == "cambiarcolor":

				os.system("cls")

				print("Esta es nuestra lista de colores: \n \n Azul  \n \n Rojo  \n \n Verde  \n \n Amarillo  \n \n Blanco")

				colorop = str(input("\nCual es tu favorito?: "))

				if colorop.lower() == "azul":

					os.system("cls")

					print( Fore.BLUE + "\nHemos cambiado el color a Azul\n")

				elif colorop.lower() == "rojo":

					os.system("cls")

					print( Fore.RED + "\nHemos cambiado el color a Rojo\n")


				elif colorop.lower() == "verde":

					os.system("cls")

					print( Fore.GREEN + "\nHemos cambiado el color a Verde\n")


				elif colorop.lower() == "amarillo":

					os.system("cls")

					print( Fore.YELLOW + "\nHemos cambiado el color a Amarillo\n")


				elif colorop.lower() == "blanco":

					os.system("cls")

					print( Fore.RESET + "\nHemos cambiado el color a Blanco\n")

			elif settingsop.lower() == "cambiar idioma" or settingsop.lower() == "cambiaridioma":

				os.system("cls")

				while go_out == False:

					print("lista de idiomas:")

					print("\nIngles (English)")

					print("\nEspañol(Spanish)")

					print("\nSalir")

					languageop = str(input("\nQue idioma quieres usar?: "))

					if languageop.lower() == "ingles" or languageop.lower() == "english":

						changelanguage = False

						os.system("cls")

						print("Necesito reiniciar antes de poder usar ",languageop,)

						op = str(input("\nEsta bien? (Si o No): "))

						if op.lower() == "si":

							language = "ENG"

							quit = True

							SPA_ENG = True

							turnoffop = False

						elif op.lower() == "no":

							os.system("cls")

							print("No reiniciaremos la aplicacion")

							time.sleep(3)

							os.system("cls")

							language = "SPA"

							afterchange_ENG = True

						else:

							go_out = True

							SPA_ENG = True

						go_out = True

					elif languageop.lower() == "español" or languageop.lower() == "spanish":

						language = "SPA"

						print("Es tu idioma actual\n ")

						go_out = True

					elif languageop.lower() == "salir":

						go_out = True

						os.system("cls")

					else:

						os.system("cls")

						print("Esa no es una opcion")

						print("\nIntenta otra vez\n")

				
			elif settingsop.lower() == "salir":

				os.system("cls")

				quit = True
			else:
				print("Que? Parece que esa no es una opcion")

				print("\n Intenta otra vez\n")

				os.system("cls")

		elif language == "ENG":

			quit == True





def menu_ENG ():

	global language

	global quit

	if language == "ENG":

		op = "none"

		os.system("cls")

		print("\nUser:",username)

		while quit == False and language == "ENG":

			print("\nMenu options:")

			print("\n-Settings")

			print("\n-Log out")

			menuop = str(input("\nWhat you want me to do?: "))

			if menuop.lower() == "settings":

				settings_ENG()

				quit = False

			elif menuop.lower() == "log out" or menuop.lower() == "logout":

				os.system("cls")

				quit = True

				if afterchange_SPA == True:

					language = "SPA"

			else:

				os.system("cls")

				print("\nHuh? Looks like thats not an option")

def menu_SPA ():

	global language

	global quit

	quit = False

	if language == "SPA":

		op = "none"

		os.system("cls")

		print("\nUsuario:",username)

		while quit == False and language == "SPA":

			print("\nMenu de opciones:")

			print("\n-Configuraciones")

			print("\n-Cerrar Sesion")

			menuop = str(input("\nQue quieres que haga?: "))

			if menuop.lower() == "configuraciones":

				settings_SPA()

			elif menuop.lower() == "cerrar sesion" or menuop.lower() == "cerrarsesion":

				os.system("cls")

				quit = True

				if afterchange_ENG == True:

					language = "ENG"

			else:

				os.system("cls")

				print("\nQue? Parece que esa no es una opcion")



def progress_bar_ENG ():

	os.system("cls")

	print("\n Loading\n")

	for i in tqdm (range(10)) :
		time.sleep(0.5)

	time.sleep(1)

	os.system("cls")

	time.sleep(1)

def progress_bar_SPA ():

	os.system("cls")

	print("\n Cargando\n")

	for i in tqdm (range(10)) :
		time.sleep(0.5)

	time.sleep(1)

	os.system("cls")

	time.sleep(1)


afterchange_ENG = (bool)

afterchange_SPA = (bool)

while check2 == False:

	if changelanguage == False:

		language = ""

	quit = False

	username = "none"

	if afterchange_SPA == True:

		Language = "SPA"

	elif afterchange_ENG == True:

		language = "ENG"

	print(Fore.RESET + "")

	afterchange_ENG = False

	afterchange_SPA = False

	if language == "":

		language = "ENG"

	if language == "ENG":

		turnoffop = True

		displayMenu_ENG()

		if language == "ENG":

			menu_ENG()

		os.system("cls")

		while quit == False or turnoffop == True:

			finalop = str(input("Want to quit the program (Yes or No)?: "))


			if finalop.lower() == "yes":

				check2 = True

				quit = True

				turnoffop = False

			elif finalop.lower() == "no":

				print( Fore.RESET + "")

				os.system("cls")

				quit = True

				turnoffop = False

				continue;

			else:

				os.system("cls")

				print("Huh? Looks like thats not an option\n")

	if language == "SPA":

		SPA_ENG = False

		quit = False

		turnoffop = True

		displayMenu_SPA()

		if language == "SPA":

			menu_SPA()

		if SPA_ENG == True:

			quit = True

		os.system("cls")

		while quit == False or turnoffop == True:

			finalop = str(input("Deseas salir del programa (Si o No)?: "))


			if finalop.lower() == "si":

				check2 = True

				quit = True

				turnoffop = False

			elif finalop.lower() == "no":

				print( Fore.RESET + "")

				os.system("cls")

				quit = True

				turnoffop = False

				continue;

			else:

				os.system("cls")

				print("Que? Parece que esa no es una opcion\n")
