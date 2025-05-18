import random
import sys

def print_diamond(N, times):
	for i in range(N):
		for ctr in range(times):
			space_ch = random.choice([chr(i) for i in range(ord(' '), ord('~')+1)])
			print(" "*(N-i),end='')
			print("*",end='')

			for j in range((i*2)-1):
				print(space_ch,end='')

			if i > 0:
				print("*",end='')
			print(" "*(N-i-1),end='')
		print()

	for i in range(N-2, -1, -1):
		space_ch = random.choice([chr(i) for i in range(ord(' '), ord('~')+1)])
		for ctr in range(times):
			print(" "*(N-i),end='')
			print("*",end='')

			for j in range((i*2)-1):
				print(space_ch,end='')

			if i > 0:
				print("*",end='')
			print(" "*(N-i-1),end='')
		print()

N = int(sys.argv[1])
for i in range(N):
	print_diamond(N,N)
