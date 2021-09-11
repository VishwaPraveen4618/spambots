import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
CHARS = string.punctuation
ALL = UPPERCASE + LOWERCASE + NUMBERS + CHARS

while True:
	length = int(input("Length: "))
	password = "".join(random.sample(ALL, length))
	print(password)