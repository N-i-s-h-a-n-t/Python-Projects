"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters."""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

#let the user enter if they are encrypting or decrypting
while True:#keep asking until user eneters e or d.
  print('Do you want to (e)ncrypt or (d)ecrypt')
  response = input('> ').lower()
  if response.startswith('e'):
    mode = 'encrypt'
    break
  if response.startswith('d'):
    mode = 'decrypt'
    break

# let user enter if they are encrypting or decrypting:
while True: #keep asking if until they enter valid key
  maKey = len(SYMBOLS) - 1
  print('Please enter the key (0 to {}) to use.'.format(maKey))
  response = input('> ').upper()
  if not response.isdecimal():
    continue

  if 0 <= int(response) < len(SYMBOLS):
    key = int(response)
    break

# let the user enter the message to encyrpt or decrypt
print('Enter the message tp {}.'.format(mode))
message = input('> ')

#Caesar cipher only work on upper case
message = message.upper()

#stores the encrypted/decrypted form of message:
translated = ''

#Encrypt/decrypt each symbol in message:
for symbol in message:
  if symbol in SYMBOLS:
    #get the encypted (or decrypted) number for this symbol
    num = SYMBOLS.find(symbol)
    if mode == 'encrypt':
      num = num + key
    elif mode == 'decrypt':
      num = num - key

    # handle the wrap around if num is larger than the length of
    # SYMBOLS or less than 0:
    if num >= len(SYMBOLS):
      num = num - len(SYMBOLS)
    elif num < 0:
      num = num + len(SYMBOLS)

    # add encrypted/decrypted number's symbol to translated:
    translated = translated + SYMBOLS[num]
  else:
    # jus add the symbol without encrypting/decrypting
    translated = translated  + symbol
  
print(translated)


