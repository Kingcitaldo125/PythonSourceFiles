def valid(s):
	mstack = []

	if len(s) == 0:
		return True

	if s[0] in [']',')','}']:
		return False

	for m in s:
		if m == "(":
			mstack.append("(")
		elif m == "{":
			mstack.append("{")
		elif m == "[":
			mstack.append("[")
		elif m == ")":
			itm = mstack.pop()
			if itm != "(":
				return False
		elif m == "}":
			itm = mstack.pop()
			if itm != "{":
				return False
		elif m == "]":
			itm = mstack.pop()
			if itm != "[":
				return False
		else:
			return False

	return len(mstack) == 0

print(valid("()"))
print(valid("()[]{}"))
print(valid("({})"))
print(valid("((()))"))
print(valid("([{}])"))

print(valid("(])"))
print(valid("{[}]"))
print(valid("((}}"))
print(valid("][]()"))
