import unittest

from has_cycle import Node, has_cycle

class Test(unittest.TestCase):
	def test_first_cycle(self):
		nnode = Node(3)
		nnode.next = Node(2)
		nnode.next.next = Node(0)
		nnode.next.next.next = Node(-4)
		nnode.next.next.next.next = nnode.next

		self.assertTrue(has_cycle(nnode))

	def test_second_cycle(self):
		nnode = Node(3)
		nnode.next = Node(2)
		nnode.next.next = nnode

		self.assertTrue(has_cycle(nnode))

	def test_third_cycle(self):
		nnode = Node(3)
		nnode.next = Node(2)
		nnode.next.next = Node(1)
		nnode.next.next.next = Node(9)
		nnode.next.next.next.next = nnode.next.next

		self.assertTrue(has_cycle(nnode))

	def test_fourth_cycle(self):
		nnode = Node(3)
		nnode.next = nnode

		self.assertTrue(has_cycle(nnode))

	def test_no_cycle1(self):
		nnode = Node(3)

		self.assertFalse(has_cycle(nnode))

	def test_no_cycle2(self):
		nnode = Node(3)
		nnode.next = Node(2)
		nnode.next.next = Node(1)
		nnode.next.next.next = Node(9)

		self.assertFalse(has_cycle(nnode))

if __name__ == '__main__':
    unittest.main()
