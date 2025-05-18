def alien_dictionary(words):
	letterdict = {}
	letterdict_keys = {}
	letterset = set([])

	for word in words:
		for w in word:
			letterdict[w] = 0
		letterset.add(w)

	for i,ls in enumerate(letterset):
		letterdict_keys[i] = []

	for word in words:
		for i,w in enumerate(word):
			letterdict[w] = max(letterdict[w],i)

	for word in words:
		for i,w in enumerate(word):
			if letterdict[w] not in letterdict_keys:
				letterdict_keys[letterdict[w]] = []

			if w in letterdict_keys[letterdict[w]]:
				continue

			letterdict_keys[letterdict[w]].append(w)

	print(f"letterdict {letterdict}")
	print(f"letterdict_keys {letterdict_keys}")

	xlist = []
	for k,v in letterdict_keys.items():
		for item in v:
			xlist.append(item)

	return "".join(xlist)

print(alien_dictionary(["z", "o"]))
print(alien_dictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
