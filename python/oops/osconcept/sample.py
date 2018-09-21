import random
guesstaken = 0
myinput = raw_input("Enter a input: ")
number=random.randint(1,20)
while guesstaken < 6:
	guess = raw_input()
	guess = int(guess)
	guesstaken=guesstaken + 1
	if guess < number:
		print "your guess is too low"
	elif guess > number:
		print "your guess is too high"
	elif guess == number:
		break
	
