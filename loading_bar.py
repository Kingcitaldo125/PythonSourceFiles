from os import system
from time import sleep

def lerp(x,y,t):
	return int(x + (y-x) * t)

def main():
	bar_width = 25
	total = 50
	for i in range(total + 1):
		system('cls')
		perc = i/total
		perc_str = str(int(perc * 100))
		lr = lerp(0,bar_width,perc)
		stars = "*" * lr
		spaces = " " * (bar_width - len(stars))
		print("[" + stars + spaces + "] " + perc_str + "%")
		sleep(1)

if __name__ == "__main__":
	main()
