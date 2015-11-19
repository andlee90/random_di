#TODO:
# a. fix roll output quotes
# b. more robust play-again loop
# c. intro menu select
# d. no 0 rolls

# script to determine the outcome(s) of any number of dice rolls
from random import randint

#--------------------------------------------------------------------------------
def dice_roller(dice, rolls, sides):

	show_di = '|   |'
	show_di_1 = '| * |'
	show_di_2 = '|* *|'
	show_di_3 = '|***|'

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
			if num_side <= 6:
				if num_side == 1:
					print '%r' % show_di_1
					print '%r' % show_di
				elif num_side == 2:
					print '%r' % show_di_2
					print '%r' % show_di
				elif num_side == 3:
					print '%r' % show_di_2
					print '%r' % show_di_1
				elif num_side == 4:
					print '%r' % show_di_2
					print '%r' % show_di_2
				elif num_side == 5:
					print '%r' % show_di_3
					print '%r' % show_di_2
				elif num_side == 6:
					print '%r' % show_di_3.strip('"\'')
					print '%r' % show_di_3.strip('"\'')
	print " "
#-----------------------------------------------------------------------------------

again_count = 0
again = "y"

while again != "n":

	if again_count < 1:
		print """
 __________________
| Dice Roller v1.0 |
| by Andrew Smith  |
|__________________|

Enter the number of dice to roll, the number
of rolls, and the number of sides per di in the 
following format: #dice #rolls #sides

--- or ---

Select from the following presets:
a. 3 man attack (Risk)
b. 2 man atack (Risk)
c. 1 man attack (Risk)
		"""
	else:
		print """

Enter the number of dice to roll, the number
of rolls, and the number of sides per di in the 
following format: #dice #rolls #sides

--- or ---

Select from the following presets:
a. 3 man attack (Risk)
b. 2 man atack (Risk)
c. 1 man attack (Risk)
		"""

	again_count += 1

	roll_choice = raw_input("> ")

	if roll_choice.isalpha():
		if roll_choice == 'a':
			dice_roller(3, 1, 6)
		elif roll_choice == 'b':
			dice_roller(2, 1, 6)
		elif roll_choice == 'c':
			dice_roller(1, 1, 6)
		else:
			print "Invalid choice.\n"

	elif roll_choice[0].isdigit():
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

	print "Would you like to roll again? y for yes, n for no"

	again = raw_input("> ")
