print("Guess a number between 1 and 100")
line = input("guess a number between 1 and 100: ")
count = 0
if line > 100:
	count = count+1
	print("your guess is too high")
elif line < 100:
	print ("your guess is number beteen 1 and 100 :", line)
elif line > 10:
	print ("your guess is too low")
else:
	pass

