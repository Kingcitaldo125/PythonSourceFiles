from collections import deque

class Minstack():
	def __init__(self):
		self.stack = deque()
		self.mtop = None
		self.min = 9999999

	def push(self, val):
		self.stack.append(val)
		self.mtop = val
		self.min = min(self.min, val)

	def pop(self):
		val = self.stack.pop()

		if val == self.min:
			self.min = min(self.stack)

		self.mtop = self.stack[-1]

		if len(self.stack) == 0:
			self.min = 9999999

	def top(self):
		return self.mtop

	def getMin(self):
		return self.min

ms = Minstack()

ms.push(3)
ms.push(-1)
ms.push(4)
ms.push(1)

print(ms.getMin())
print(ms.top())

for i in range(3):
	ms.pop()

print(ms.getMin())
print(ms.top())
