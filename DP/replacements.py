"""
https://github.com/hoaiphun96/Prepare-For-Coding-Interviews/blob/master/Dynamic%20Programming/integerRearrangement.py
Given a positive integer n and you can do operations as follow:
If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
Example 1:
Input:
8
Output:
3
Explanation:
8 -> 4 -> 2 -> 1
Example 2:
Input:
7
Output:
4
Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""

from collections import defaultdict
from sys import argv

def replacements(n):
	cache = defaultdict(int)

	def r_help(N):
		if N in cache:
			return cache[N]

		if N <= 1:
			cache[N] = 0
			return 0
		elif N == 2:
			cache[N] = 1
			return 1
		elif N == 4:
			cache[N] = 2
			return 2

		if N % 2 == 0:
			nhalf = N//2
			xo = 1 + r_help(nhalf)
			cache[N] = xo
			return xo

		xn = 1 + min(r_help(N+1), r_help(N-1))

		cache[N] = xn

		return xn

	return r_help(n)

N = int(argv[1])

print(f'replacements({N}) = {replacements(N)}')
