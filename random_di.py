# script to determine the outcome(s) of any number of dice rolls
from random import randint

#--------------------------------------------------------------------------------
def dice_roller(dice, rolls, sides):

	roll_counter = 0
	di_counter = 0

	while roll_counter < rolls:
		roll_counter+=1
		di_counter = 0
		print " "

		while di_counter < dice:
			di_counter+=1
			num_side = randint(0, sides)
			print "Roll %r, Di %r: %r" % (roll_counter, di_counter, num_side)
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
