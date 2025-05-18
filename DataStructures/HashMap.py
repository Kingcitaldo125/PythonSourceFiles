from hashlib import sha256
from random import randrange as rr

class HashMap:
	def __init__(self):
		initial_size = 100
		self.marray = [[] for i in range(initial_size)]
		self.size = initial_size
		self.num_items = 0
		self.keys = set()
		self.load_factor = None

		self._update_load_factor()

	def _increase_size(self):
		increase_factor = 0.25

		for i in range(int(self.size // increase_factor)):
			self.marray.append([])

		self.size = len(self.marray)
		print(f"New size: {self.size}")

	def _update_load_factor(self):
		self.load_factor = self.num_items / self.size

	def get_hash_idx(self, k):
		sv = 0
		mhash = sha256()
		mhash.update(bytes(str(k), 'utf-8'))
		mhash = mhash.hexdigest()

		for i in range(len(str(k))):
			sv += ord(mhash[i])

		return sv % self.size

	def add(self, k, v):
		hidx = self.get_hash_idx(k)

		if k in self.keys:
			raise ValueError(f"Already have key '{k}' in store.")

		print(f"hidx {hidx}")

		self.marray[hidx].append((k,v))

		self.keys.add(k)

		self.num_items += 1

		self._update_load_factor()

		print(f"load_factor {self.load_factor}")

		if self.load_factor > 0.7:
			#print("Increasing size")
			self._increase_size()

	def get(self, k):
		hidx = self.get_hash_idx(k)

		if hidx < 0 or hidx >= self.size:
			raise IndexError(f"Cannot find key {k} in map")

		for i in self.marray[hidx]:
			if i[0] == k:
				return i[1]
		return -1

def main():
	hm = HashMap()

	#itms = [27, 21, 75, 94, 84, 91, 57, 22, 70, 85]
	itms = [rr(1,100) for i in range(20)]

	for i in itms:
		try:
			print(f"Adding {i}")
			hm.add(i, str(i))
		except ValueError as e:
			print(e)
			continue

		print("")

	for i in itms:
		print(i, hm.get(i))

if __name__ == "__main__":
	main()
