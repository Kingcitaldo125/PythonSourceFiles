from itertools import permutations as permutes

def check_inclusion(s1, s2):
	perms = ["".join([b for b in a]) for a in list(permutes(s1))]
	
	for p in perms:
		if p in s2:
			return True
	return False

res = check_inclusion("abc", "lecaabee")

print("yes" if res == True else "no")
