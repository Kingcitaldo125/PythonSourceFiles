x = 1
numb = int(input("Enter Number:\n"))
ones = 0
zeros = 0

dword = 4294967296

while x < dword:
	if x & numb == x:
		ones += 1
	else:
		zeros += 1
	x=x<<1

print(f"Zeros: {zeros}")
print(f"Ones: {ones}")
