class Heap:
	def __init__(self):
		self.data = []

	def get_size(self):
		return len(self.data)

	def _get_item(self, idx):
		return self.data[idx]

	def _get_parent(self, itm):
		idx = (itm - 1) // 2
		if idx < 0:
			return -1
		return idx

	def getLeftChild(self, idx):
		return 2 * idx + 1

	def getRightChild(self, idx):
		return 2 * idx + 2

	def add_node(self, val):
		self.data.append(val)
		self.heapify_up(self.get_size() - 1)

	def swap(self, l, r):
		self.data[l], self.data[r] = self.data[r], self.data[l]

	def heapify_up(self, idx):
		while 1:
			pidx = self._get_parent(idx)

			if idx < 0 or pidx < 0:
				#print(f'bottom out {idx} {pidx}')
				break

			val = self._get_item(idx)
			parent = self._get_item(pidx)

			if parent <= val:
				break

			self.swap(pidx, idx)

			idx = self._get_parent(idx)

	def heapify_down(self):
		idx = 0

		while 1:
			lc = self.getLeftChild(idx)

			if lc >= self.get_size():
				break

			mlc = self._get_item(lc)

			rc = self.getRightChild(idx)
			mrc = self._get_item(rc)

			if rc >= self.get_size():
				mrc = 999999999

			mitm = self._get_item(idx)

			min_item = min(mlc, mrc)
			min_idx = lc

			if min_item == mrc:
				min_idx == rc

			if mitm < min_item:
				break

			self.swap(idx, min_idx)

			if min_item == mlc:
				idx = lc
			else:
				idx = rc

	def peek(self):
		if self.get_size() < 1:
			return -1
		return self.data[0]

	def poll(self):
		if self.peek() == -1:
			return -1

		xitm = self.peek()
		gz = self.get_size() - 1

		if gz < 1:
			return xitm

		self.data[0] = self._get_item(gz)
		self.data.pop()

		self.heapify_down()

		return xitm

	def print_(self):
		print(self.data)

xlist = [29, 11, 33, 38, 25, 19, 10, 7, 42, 35, 46, 18, 29, 34, 43]

h = Heap()

for x in xlist:
	h.add_node(x)

h.print_()

h.poll()

h.print_()
