def validPal(s):
	s_alnum = [i.lower() for i in s if i.isalnum()]
	return s_alnum==s_alnum[::-1]

if __name__ == "__main__":
	print(validPal("Red rum, sir, is murder"))
	print(validPal("Programcreek is awesome"))