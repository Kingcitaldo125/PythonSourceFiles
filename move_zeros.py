def move_zeros(mlist):
	si = 0
	end_ptr = len(mlist) - 1

	while 1:
		if si >= len(mlist):
			break

		itm = mlist[si]
		if itm == 0:
			scurr = si
			snext = scurr + 1

			while scurr < end_ptr:
				mlist[scurr], mlist[snext] = mlist[snext], mlist[scurr]
				scurr += 1
				snext += 1

			end_ptr -= 1

		si += 1

if __name__ == "__main__":
	ml = [0, 1, 4, 0, 7, 7, 2, 0, 3, 0, 7, 1]
	move_zeros(ml)
	print(ml)
