import math

i = 0

while 1:
	if i >= math.pi*2:
		break

	print(i, math.degrees(math.atan2(math.sin(i), math.cos(i))))

	i += ((2*math.pi)/5)
