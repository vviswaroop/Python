def div42by(divideby):
	try:
		return 42 / divideby
	except ZeroDivisionError:
		print('Error: you tried to divide by zero')
print(div42by(2))
print(div42by(42))
print(div42by(0))
print(div42by(1))
