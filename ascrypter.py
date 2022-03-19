import string
import sys
from secret import flag


def sifrele(msg):
	ct = []
	for char in msg:
		ct.append(ord(char) + 5)
	return ct

sys.stdout = open('crypted.txt', "w")
print(*sifrele(flag), sep=" ")