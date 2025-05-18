class PrefixTree:
	def __init__(self):
		self.data = {}
		self.words = set([])

	def insert_help(self, word, dat):
		if len(word) < 1:
			return

		for i,w in enumerate(word):
			if w not in dat:
				dat[w] = {}
				self.insert_help(word[i+1:], dat[w])
				self.data = dat
				return

			dat = dat[w]

	def insert(self, word):
		dat = self.data
		self.insert_help(word, dat)
		self.words.add(word)

	def search(self, word):
		return word in self.words

	def starts_with_help(self, prefix, dat):
		if len(prefix) < 1:
			return True

		if prefix[0] not in dat:
			return False

		return self.starts_with_help(prefix[1:], dat[prefix[0]])

	def starts_with(self, prefix):
		dat = self.data
		return self.starts_with_help(prefix, dat)

if __name__ == "__main__":
	tree = PrefixTree()
	tree.insert("dog")
	print(tree.search("dog"))
	print(tree.search("do"))
	print(tree.starts_with("do"))
	print(tree.starts_with("cat"))
	tree.insert("do")
	print(tree.search("dog"))
	print(tree.search("do"))
