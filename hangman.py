word = "HANGMAN"


guessed = False
underscore_list = []
tries = 5

for i in word:
	underscore_list.extend(["_"])

print(underscore_list)

word_list = list(word)
while guessed == False and tries != -1:
	temp_guess = 0
	guess = input("Enter a letter or the full word\n")
	guess = guess.upper()
	if len(guess) == 1:
		for i,letter in enumerate(word_list):
			if letter == guess:
				underscore_list[i] = letter
				temp_guess += 1
		if temp_guess == 0:
			print("Incorrect, you have " + str(tries) + " more tries\n")
			tries -= 1
		else:
			print(underscore_list)
	elif len(guess) > 1:
		if guess == word:
			guessed = True
			print("You win!")
			break
		else:
			print("Incorrect, you have " + str(tries) + " more tries\n")
			tries -= 1
	if ("_" in underscore_list) == False:
		guessed = True
		print("You win")

if tries == -1:
	print("You lose, try again!")