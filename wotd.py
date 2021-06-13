#Importing extras
import random
import replit

#Defining the logo
logo = ''' __     __     ______     ______     _____        ______     ______      ______   __  __     ______        _____     ______     __  __        ______     __  __     __     ______    
/\ \  _ \ \   /\  __ \   /\  == \   /\  __-.     /\  __ \   /\  ___\    /\__  _\ /\ \_\ \   /\  ___\      /\  __-.  /\  __ \   /\ \_\ \      /\  __ \   /\ \/\ \   /\ \   /\___  \   
\ \ \/ ".\ \  \ \ \/\ \  \ \  __<   \ \ \/\ \    \ \ \/\ \  \ \  __\    \/_/\ \/ \ \  __ \  \ \  __\      \ \ \/\ \ \ \  __ \  \ \____ \     \ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__  
 \ \__/".~\_\  \ \_____\  \ \_\ \_\  \ \____-     \ \_____\  \ \_\         \ \_\  \ \_\ \_\  \ \_____\     \ \____-  \ \_\ \_\  \/\_____\     \ \___\_\  \ \_____\  \ \_\   /\_____\ 
  \/_/   \/_/   \/_____/   \/_/ /_/   \/____/      \/_____/   \/_/          \/_/   \/_/\/_/   \/_____/      \/____/   \/_/\/_/   \/_____/      \/___/_/   \/_____/   \/_/   \/_____/'''

#Setup main menu
print(logo)
print(" ")
print("TYPE ALL ANSWERS EXACTLY AS WRITTEN!")
print("Play")
print("Instructions \n")
action = str(input("Type 'Play' or 'Instructions': "))

#Option choose results
if action.lower() == "instructions":
	replit.clear()
	print("You and your group will recieve a series of questions, based upon the word of days from the 2020 - 2021 school year.\nYou must type your answers EXACTLY as shown.\nThis includes any punctuation.\nWhen you finish all 13 questions, take the first letter of all of your answer choices, and rearrange them to form a word of the day.\nThe first group to do so, claims the victory.\nLeave the breakout room and respond with the word.")
	moveOn = input(" ")
	replit.clear()
	print(logo)
	print(" ")
	print("TYPE ALL ANSWERS EXACTLY AS WRITTEN!")
	action = str(input("Type 'Play' or 'Instructions': "))

if action.lower() == "play":
	replit.clear()
	questions = 0
	score = 0
	code_final = "schadenfreude"
	#q1
	print("Sycophant\nLoquacious\nLigneous\nPensive\n")
	questions += 1
	q1 = str(input("Which of the following words is a noun?\n(Type the word and hit enter. Any capitalization will work.): "))
	if q1.lower() == "sycophant":
		score += 1
		correctPopup = input("Correct. Press enter to continue.")
		#q2
		replit.clear()
		print("Empyrean\nOrwellian\nDraconian\nLuddite\n")
		questions += 1
		q2 = str(input("Which of the words above means 'excessively harsh and severe'\n(Type the word and hit enter. Any capitalization will work.): "))
		if q2.lower() == "draconian":
			correctPopup = input("Correct. Press enter to continue.")
			#q3s
			replit.clear()
			print("Avant-Garde\nCernuous\nAntediluvian\nAcrimonious\n")
			q3 = str(input("Which of the words above has a French origin?\n(Type the word and hit enter. Any capitalization will work.): "))
			if q3.lower() == "avant-garde":
				correctPopup = input("Correct. Press enter to continue.")
				#q4
				replit.clear()
				print("Impugn\nMajuscule\nDefenestration\nImportune\n")
				q4 = str(input("Which of the following means 'The action of throwing someone out of a window'?\n(Type the word and hit enter. Any capitalization will work.): "))
				if q4.lower() == "defenestration":
					correctPopup = input("Correct. Press enter to continue.")
					#q5
					replit.clear()
					print("Echelon\nTorpor\nImportune\nEmpyrean\n")
					q5 = str(input("Which of the following is an adjective?\n(Type the word and hit enter. Any capitalization will work.): "))
					if q5.lower() == "empyrean":
						correctPopup = input("Correct. Press enter to continue.")
						#q6
						replit.clear()
						print("Apoplectic\nLaissez-Faire\nNarcissism\nEclectic\n")
						q6 = str(input("Which of the following would be a good quality for a person to have?\n(Type the word and hit enter. Any capitalization will work.): "))
						if q6.lower() == "eclectic":
							correctPopup = input("Correct. Press enter to continue.")
							#q7
							replit.clear()
							q7 = str(input)
						else:
							print("Incorrect. GAME OVER")
					else: 
						print("Incorrect. GAME OVER")	
				else:
					print("Incorrect. GAME OVER")
			else:
				print("Incorrect. GAME OVER")
		else:
			print("Incorrect. GAME OVER")
	else:
		print("Incorrect. GAME OVER")

