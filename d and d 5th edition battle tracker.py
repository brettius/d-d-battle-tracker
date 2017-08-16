import pickle

print('Barbarian Battle Tracker')

def main():
	
	player_stats = {'HP': 0, 'Max HP' : 0 ,'Hit Dice': 0, 'Exp': 0, 
	'Rages':0}
	
	run = True

	while run == True:
			
		player_stats_print_dictionary(player_stats)	
		menu = main_menu()
		
		if menu == 1:
			player_stats['HP'] = damage(player_stats['HP'])
		elif menu == 2:
			player_stats['HP'] = heal(player_stats['HP'])	
		elif menu == 3:
			saving_throws()
		elif menu == 4:
			player_stats['Hit Dice'] = hits(player_stats['Hit Dice'])
		elif menu == 5:
			player_stats['Rages'] = rage_amount(player_stats['Rages'])
		elif menu == 6:
			player_stats  = update(player_stats)
		elif menu == 7:
			save_file(player_stats)
		elif menu ==8:
			player_stats = open_file()
		elif menu ==10:
			run = False
			
#Print dictionary

def player_stats_print_dictionary(player_stats):

	print('-------------------')
	print('HP:', 
	player_stats['HP'], '/', 
	player_stats['Max HP'], '\tExp:',
	player_stats['Exp'], '\tHit Dice:',
	player_stats['Hit Dice'],'\tRages:',
	player_stats['Rages'],'\n')
		
#Hit points, take damage

def damage(hit_points):
	
	try:	
		damage = int(input('Damage'))
	except:
		print('Incorrect entry')
	else:
		hit_points -= damage
		return hit_points
		
#Hit points, heal

def heal(hit_points):
	
	try:
		heal = int(input('Heal'))
	except:
		print('Incorrect entry')
	else:
		hit_points += heal
		return hit_points
			
#Death saving throws secondary menu
		
def saving_throws():
	
	death_saves = 0
	life_saves = 0

	saves = True

	while saves == True:	
			
		#Calculate if player stabilizes or dies
		
		print('Death saves:', life_saves)
		print('Death faliures:', death_saves)
		if death_saves == 3:
			print('You die')
			break
		elif life_saves ==3:
			print('You stabilize')
			break
			
		#Get user input for saving or failing
		
		print('\n1. Succeed at the throw')
		print('2. Fail at the throw')
		print('3. Exit to main menu')
		try:
			save = int(input('\nEnter choice\n'))
		except:
			print('Incorrect entry')
		else:
			if save == 1:
				life_saves += 1
			elif save == 2:
				death_saves += 1
			else:
				saves = False
				
#Hit dice secondary menu
			
def hits(hit_dice):	
				
	print('Current hit dice:', hit_dice)
	print('\n1. Use hit dice')
	print('2. Regain hit dice')
		
	try:
		hit_dice_choice = int(input('Enter choice'))
	except:
		print('Incorrect entry')
	else:
		if hit_dice_choice == 1:
			hit_dice -= 1
		elif hit_dice_choice == 2:
			hit_dice += 1
		return hit_dice
			
#Rages seconday menu			
	
def rage_amount(rages):
	print('1. Use a rage')
	print('2. Regain a rage\n')
	try:	
		choice = int(input('Enter choice'))
	except:
		print('Incorrect entry')
	else:
		if choice == 1:
			rages -= 1
		elif choice == 2:
			rages += 1
		return rages
		
#Update character with hit points, experience, and rages
	
def update(all_stats):
				
		print('1. Enter hit points')
		print('2. Enter max hit points')
		print('3. Enter hit dice')
		print('4. Enter experience')
		print('5. Enter rages')
		
		try:
			update = int(input('Enter choice'))
		except:
			print('Enter a valid number')
		else:
			if update == 1:
				all_stats['HP'] = int(input('Enter current hit points\n'))
			elif update == 2:
				all_stats['Max HP'] = int(input('Enter max hit points'))
			elif update == 3:
				all_stats['Hit Dice'] = int(input('Enter hit dice'))	
			elif update == 4:		
				all_stats['Exp'] = int(input('Enter experience'))
			elif update == 5:
				all_stats['Rages']= int(input('Enter rages'))
			
		return all_stats
			
#Write to the save file
		
def save_file(player_stats):
	try:
		output = open('tracker.dat','wb')
	except:
		print('Error has occured')
	else:
		pickle.dump(player_stats, output)
		output.close()
#Open the save file
		
def open_file():
	try:
		input_file = open('tracker.dat','rb')
	except:
		print('Error has occured')
	else:
		player_stats = pickle.load(input_file)
	
		return player_stats
		
def main_menu():
	
	print('1. Damage')
	print('2. Heal')
	print('3. Death saves')
	print('4. Hit dice')
	print('5. Use a rage')
	print('-------------------')
	print('6. Update character')
	print('7. Save')
	print('8. Load')
	print('10. Quit\n')
	
	try:
		menu = int(input('Enter choice\n'))
	except:
		print('Incorrect entry')
	else:	
		return menu
		
#Run program	

main()
