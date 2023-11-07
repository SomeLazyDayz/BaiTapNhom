letter = input("Enter a Letter: ")

if letter in ['a', 'e', 'i', 'o', 'u']:
	print("%c is a vowel" % letter)
elif letter == 'y':
	print("Sometimes y is vowel & sometimes consonant")
elif letter in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']:
	print("%c is a consonant" % letter)
else:
	print("%c is not a letter" % letter)