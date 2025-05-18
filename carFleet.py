def carFleet(target, position, speed):
	len_items = len(position)

	max_pos = 0
	max_speed = 0
	fleets = 0
	for it in range(len_items):
		pos = position[it]
		spd = speed[it]

		#print("max_pos", max_pos)
		#print("max_speed", max_speed)

		if spd >= max_speed:
			max_speed = max(max_speed, spd)
			fleets += 1
		elif pos <= max_pos:
			fleets += 1

		pos = max(max_pos, pos)
		#print()

	return fleets

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(carFleet(10, [3], [3]))
print(carFleet(100, [0,2,4], [4,2,1]))
