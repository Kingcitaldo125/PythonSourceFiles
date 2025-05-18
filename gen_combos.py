import sys

def gen_combos_help(xlist, comboset, mstr, idx):
	if idx >= len(mstr)//2:
		return

	for i in range(len(xlist)):
		xlc = [x for x in xlist]

		if xlc[0] != '(':
			xlc.insert(i,'(')

		for j in range(i + 2, len(xlc) + 1):
			rlc = [x for x in xlc]
			if rlc[0] != ')':
				rlc.insert(j,')')
			try:
				jstr = "".join(rlc)

				eval(jstr)
				comboset.add(jstr)
			except:
				continue

			gen_combos_help(rlc, comboset, mstr, idx + 1)

def gen_combos(mstr):
	comboset = set([])
	xlist = [m for m in mstr]

	gen_combos_help(xlist, comboset, mstr, 0)

	print(f"comboset {comboset}")
	resset = set([])

	for combo in comboset:
		resset.add(eval(combo))

	return list(resset)

if len(sys.argv) < 2:
	print("Please specify input")
	sys.exit(1)

cbos = gen_combos(sys.argv[1])

print(f"cbos {cbos}")

sys.exit(0)
