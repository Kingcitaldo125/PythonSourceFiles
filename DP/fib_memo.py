from collections import defaultdict

def fib(N):
	if N == 0:
		return 0

	if N == 1 or N == 2:
		return 1

	return fib(N-2) + fib(N-1)

def fib_memo(N):
	items = defaultdict(int)

	def fib_h(N):
		if N == 0:
			return 0

		if N == 1 or N == 2:
			return 1

		if N in items:
			return items[N]

		items[N] = fib_h(N-2) + fib_h(N-1)

		return items[N]

	return fib_h(N)

if __name__ == "__main__":
	for i in range(100):
		print(i,fib_memo(i))
