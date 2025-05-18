#https://leetcode.com/problems/trapping-rain-water/
def trap_water(mlist):
	water_tile_count = 0
	cur_max = 0
	it = 0

	while 1:
		if it >= len(mlist):
			break

		mid = mlist[it]

		if mid > cur_max:
			cur_max = mid
			#print(f"cur_max {cur_max}")

		if mid < cur_max:
			cur_count = 0
			did_break = False
			li = 0

			for i in range(it, len(mlist)):
				local_item = mlist[i]
				#print(f"local_item {local_item}")
				if local_item >= cur_max:
					did_break = True
					li = i
					#print(f"li {li}")
					break
				cur_count += (cur_max - local_item)

			if did_break:
				water_tile_count += cur_count
				print(f"water_tile_count {water_tile_count}")
				it += li - it
				continue

			li = 0
			for i in range(it,len(mlist)-1):
				subleft = mlist[i-1]
				submid = mlist[i]
				subright = mlist[i+1]

				"""
				print(f"subleft {subleft}")
				print(f"submid {submid}")
				print(f"subright {subright}")
				"""

				if submid < subleft and submid < subright:
					water_tile_count += (min(subleft, subright) - submid)
					print(f"nested water_tile_count {water_tile_count}")
					li = i
					break
			it += li

		it += 1
		print("")

	return water_tile_count

#print(trap_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap_water([0,2,0,2,0,1,0]))
