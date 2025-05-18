import random

num = int(input("How Many?\n"))

with open('out.txt','w') as f:
	for i in range(num):
		f.write(str(random.randrange(1,1000)))
		f.write('\n')

print(f"Wrote '{num}' numbers to the file.")
