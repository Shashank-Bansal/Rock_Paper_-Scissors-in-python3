import time
import random

def choice (t):
	time.sleep(.7)
	if t is 0:
		print("###### PAPER #####\n")
	elif t is 1:
		print("##### ROCK #####\n")
	elif t is 2:
		print("##### SCISSORS #####\n")
	time.sleep(.9)

c = d = e = 0

name=input("Enter your name here: ")
print("\nWelcome to the game, " +name+ "!")
time.sleep(.9)
print("How to play: ")

while(1):
	time.sleep(.9)
	print('Please press one of the key of which discription is given below')
	time.sleep(.7)
	print("Press '0' if you want to choose paper")
	time.sleep(.7)
	print("Press '1' if you want to choose rock")
	time.sleep(.7)
	print("Press '2' if you want to choose scissors")
	time.sleep(.7)
	print("Press '3' if you want to exit ")
	time.sleep(.7)
	try:
		a = int(input('Enter your move: '))
		if a < 0 or a > 3:
			print("\n*****Invalid move*****\nTry again\n")
			continue
	except:
		print("\n*****Invalid move*****\nTry again\n")
		continue
	if a is 3:
		print("\n##### "+name+" WANTS TO EXIT #####\n")
		break
	b = random.randrange(0,2)
	time.sleep(1.2)
	print('\nRock ! Paper ! Scissors !.......')
	time.sleep(0.9)
	print('\n'+name+"'s choice is :")
	choice(a)
	print("Computer's choice is :")
	choice(b)
	if a is 0 and b is 1:
		print("*******"+name+" WINS********\n")
		c+=1
	elif a is 0 and b is 0:
		print("*******DRAWS*******\n")
		d+=1
	elif a is 0 and b is 2:
		e+=1
		print("*******COMPUTER WINS*******\n")
	elif a is 1 and b is 0:
		print("*******COMPUTER WINS********\n")
		e+=1
	elif a is 1 and b is 1:
		print("******DRAWS*******\n")
		d+=1
	elif a is 1 and b is 2:
		print("*******"+name+" WINS********\n")
		c+=1
	elif a is 2 and b is 0:
		print("*******"+name+" WINS********\n")
		c+=1
	elif a is 2 and b is 1:
		print("******COMPUTER WINS******\n")
		e+=1
	elif a is 2 and b is 2:
		print("******DRAWS*******\n")
		d+=1
	time.sleep(1.3)
	print('Score:-\n	'+name+': '+str(c)+'		Draws: '+str(d)+'		Computer:'+str(e))
	print("\n######################################### NEXT TURN ######################################\n")
time.sleep(.9)
print('*******FINAL SCORE*******')
time.sleep(.7)
print('	'+name+': '+str(c)+'		Draws: '+str(d)+'		Computer:'+str(e))
time.sleep(.7)
if c > e:
	print('\n******* Congatulations!, You Win! *******\n')
elif c == e:
	print('\n***** DRAW *****')
	time.sleep(.7)
	print('\nTry again to play to win!\n')
else:
	print('\n*** Computer Win! ***\n')
	time.sleep(.7)
	print('Try again to play to win!\n')
