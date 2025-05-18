def bin_flip(N):
	nbin = bin(N)[2:]
	nbin_list = [i for i in '0'*(32 - len(nbin)) + nbin]
	nbin_list_flip = []

	for n in nbin_list:
		nbin_list_flip.append('0' if n == '1' else '1')
	
	print("nbin_list_flip",nbin_list_flip)
	npow = 0
	ctr = 0
	for n in nbin_list_flip[::-1]:
		if n == '1':
			npow += 2**ctr
		ctr += 1

	return npow

print(bin_flip(4))
