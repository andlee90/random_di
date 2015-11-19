# script to determine the outcome(s) of any number of dice rolls
# by Andrew Smith (2015)

from random import randint

#---------dice_roller function to determine roll outcomes----------------------------
def dice_roller(dice, rolls, sides):

	show_di = '|   |'
	show_di_1 = '| * |'
	show_di_2 = '|* *|'
	show_di_3 = '|***|'
	show_di_t = ' ___ '
	show_di_b = ' --- '

	roll_counter = 0
	di_counter = 0

	while roll_counter < rolls:
		roll_counter+=1
		di_counter = 0
		print " "

		while di_counter < dice:
			di_counter+=1
			num_side = randint(1, sides)
			print "Roll %r, Di %r: %r" % (roll_counter, di_counter, num_side)
			if num_side <= 6: # print di symbol if di is six-sided
				if num_side == 1:
					print show_di_t
					print show_di_1
					print show_di
					print show_di_b
				elif num_side == 2:
					print show_di_t
					print show_di_1
					print show_di_1
					print show_di_b
				elif num_side == 3:
					print show_di_t
					print show_di_1
					print show_di_2
					print show_di_b
				elif num_side == 4:
					print show_di_t
					print show_di_2
					print show_di_2
					print show_di_b
				elif num_side == 5:
					print show_di_t
					print show_di_2
					print show_di_3
					print show_di_b
				elif num_side == 6:
					print show_di_t
					print show_di_3
					print show_di_3
					print show_di_b
	print " "
#-----------------------------------------------------------------------------------
title = """
 __________________
| Dice Roller v1.1 |
| by Andrew Smith  |
|__________________|
"""

menu = """
Enter the number of dice to roll, the number
of rolls, and the number of sides per di in the 
following format: #dice #rolls #sides

--- or ---

Select from the following presets:

a. 3 man attack (Risk)
b. 2 man attack or defend (Risk)
c. 1 man attack or defend (Risk)

--- or ---

Type 'menu' to repeat this menu

--- or ---

Type 'quit' to quit
		"""
print title
print menu

again = 0

while again != 1: # prompts the user until 'quit' is entered

	roll_choice = raw_input("> ")

	if roll_choice.isalpha(): # if input starts with a letter
		if roll_choice == 'a':
			dice_roller(3, 1, 6)
		elif roll_choice == 'b':
			dice_roller(2, 1, 6)
		elif roll_choice == 'c':
			dice_roller(1, 1, 6)
		elif roll_choice == 'menu':
			print menu
		elif roll_choice == 'quit':
			again = 1
		else:
			print "Invalid choice.\n"

	elif roll_choice[0].isdigit(): # if input starts with a number
		choices = roll_choice.split()
		size = len(choices)
		if size == 3:
			one = int(choices[0])
			two = int(choices[1])
			three = int(choices[2])
			dice_roller(one, two, three)
		else:
			print "Invalid Choice.\n"
	else:
		print "Invalid choice.\n"
