import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
	# Returns a string of unique random digits that is NUM_DIGITS long.
	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum = ''
	for i in range(NUM_DIGITS):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	# Returns a string with the Pico, Fermi, & Bagels clues to the user.
	if guess == secretNum:
		return 'You Got It!'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels'

	clues.sort()
	return ' '.join(clues)

def isOnlyDigits(num):
	#Returns True if num is a string of only digits. Otherwise,
	# returns False
	if num == '':
		return False
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False

	return True

print(f'I am thinking of a {NUM_DIGITS} digit number. Try to guess what it is')
print('The clues I give are...')
print('When I say:     That means:')
print('----------      ----------')
print('  Bagels    -   None of the digits are correct')
print('  Pico      -   One digit is correct but in the WRONG position')
print('  Fermi     -   One digit is correct and in the RIGHT position')

while True:
	secretNum = getSecretNum()
	print(f'I have thought up a number. You have {MAX_GUESS} guesses to get it!')

	guessesTaken = 1
	while guessesTaken <= MAX_GUESS:
		guess = ''
		while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
			print(f'Guess #{guessesTaken}: ')
			guess = input()

		print(getClues(guess, secretNum))
		guessesTaken += 1

		if guess == secretNum:
			break
		if guessesTaken > MAX_GUESS:
			print(f'You ran out of guesses! The answer was {secretNum}')

	print('Do you want to play again? (yes or no)')
	if not input().lower().startswith('y'):
		break





