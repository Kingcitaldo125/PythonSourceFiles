from lcs import longest_common_substring as lcs

import unittest

class TestLCS(unittest.TestCase):
	def testNone(self):
		self.assertTrue(lcs("abc", "def") == 0)

	def testEqual(self):
		self.assertTrue(lcs("abc", "abc") == 3)

	def testACE(self):
		self.assertTrue(lcs("abcde", "ace") == 3)

	def testTwoLen(self):
		self.assertTrue(lcs("joker", "je") == 2)

	def testFire(self):
		self.assertTrue(lcs("firewalls", "fall") == 4)

	def testNine(self):
		self.assertTrue(lcs("ninety", "nine") == 4)

	def testLongString(self):
		self.assertTrue(lcs("plwprtimilwafefbeenviorunqjmrjvocthupubckyclheejdx", "milwaukee") == 9)

	def testEmptyBase(self):
		self.assertTrue(lcs("", "long") == 0)

	def testEmptySub(self):
		self.assertTrue(lcs("retrieve", "") == 0)

	def testEmptyEmpty(self):
		self.assertTrue(lcs("", "") == 0)

if __name__ == "__main__":
	unittest.main()
