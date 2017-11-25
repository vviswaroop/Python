print('How many cats you have?')
numCats = input()
try:
	if int(numCats) >= 4:
		print('There is a lot of cats')
	else:
		print('that is not too many cats')
except NameError:
	print('You did n ot enter a number')
