from os import system
from random import choice
from time import sleep

def lerp(a,b,c):
	return a + (b-a) * c

def pybar(limit):
	ctr = 0
	bar_len = 50
	pad_char = choice(['#', '@', '-'])

	for i in [i for i in range(1,limit)]:
		for j in range(1,limit):
			i % j

		system("cls")

		divv = ctr/limit
		npads = divv
		npads = int(lerp(2, bar_len, npads))

		pads = pad_char * npads
		spaces = " " * (bar_len - npads)

		print("[" + pads + spaces + "] " + str(round(divv*100,2))+"%")

		ctr += 1

	ctr += 1

	system("cls")

	divv = ctr/limit
	npads = divv
	npads = int(lerp(2, bar_len, npads))

	pads = pad_char * npads
	spaces = " " * (bar_len - npads)

	print("[" + pads + spaces + "] " + str(round(divv*100,2))+"%")

pybar(500)
