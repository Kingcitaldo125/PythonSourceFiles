def reverse_int(x):
	if x > -10 and x < 10:
		return x

	signed = False
	x_str = str(x)
	mask = 0xFFFFFFFF

	if x_str[0] == '-':
		signed = True

	mint = int(x_str[::-1].strip('0-'))

	if mask & mint != mint:
		return 0

	return mint * -1 if signed else mint

print(reverse_int(-8))
print(reverse_int(5))
print(reverse_int(10))
print(reverse_int(11))
print(reverse_int(123))
print(reverse_int(-123))
print(reverse_int(120))
