#insta : @g.vuw
import random
def GetPassword(data):
	x = 8
	password = ""
	while len(password)!= x :
		value = random.choice(data)
		password += value
	return password

data ='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(20000):
	    print(GetPassword(data))
	    