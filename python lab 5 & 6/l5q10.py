#!/usr/bin/python3
def encrypt(z,s):
	result = ""
	for i in range(len(z)):
		char = z[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
z = str(input("Enter String:"))
s = 4
print ("z : " + z)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(z,s))
