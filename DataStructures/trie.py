from collections import defaultdict

class Trie:
	def __init__(self):
		self.nodes = defaultdict(Trie)
		self.is_leaf = False
		self.words = []

	def insert(self, word):
		c_node = self

		for i in word:
			if i not in c_node.nodes:
				c_node.nodes[i] = Trie()
			c_node = c_node.nodes[i]

		self.words.append(word)
		c_node.is_leaf = True

	def search(self, word):
		c_node = self

		for w in word:
			if w not in c_node.nodes:
				return False
			c_node = c_node.nodes[w]

		return c_node.is_leaf

	def print_words(self):
		print(self.words)

trie = Trie()

trie.insert('hello')
trie.insert('search')
trie.insert('insert')

trie.print_words()
