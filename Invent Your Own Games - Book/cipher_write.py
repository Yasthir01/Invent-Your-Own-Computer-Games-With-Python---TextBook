#Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
	while True:
		print('Do you wish to encrypt or decrypt or brute force a message?')
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd']:
			return mode
		else:
			print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
	print('Enter your message: ')
	return input()

def getKey():
	key = 0
	while True:
		print(f'Enter the key number (1 - {MAX_KEY_SIZE})')
		key = int(input())
		if key >=1 and key <= MAX_KEY_SIZE:
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''

	for symbol in message:
		symbolIndex = SYMBOLS.find(symbol)
		if symbolIndex == -1: #Symbol not found in SYMBOLS
			#Just add this symbol without any change
			translated += symbol
		else:
			#Encrypt or Decrypt
			symbolIndex += key

			if symbolIndex >= len(SYMBOLS):
				symbolIndex -= len(SYMBOLS)
			elif symbolIndex < 0:
				symbolIndex += len(SYMBOLS)

			translated += SYMBOLS[symbolIndex]
	return translated

mode = getMode()
message = getMessage()
key = getKey()
if mode[0] != 'b':
	key = getKey()
print('Your translated text is: ')
if mode[0] != 'b':
	print(getTranslatedMessage(mode, message, key))
else:
	for key in range(1, MAX_KEY_SIZE + 1):
		print(key, getTranslatedMessage('decrypt', message, key))




