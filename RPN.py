def is_operand(i):
	return i == '+' or i == '-' or i == '*' or i == '/'

def RPN(items):
	mstack = []

	for itm in items:
		if is_operand(itm):
			i2 = float(mstack.pop())
			i1 = float(mstack.pop())

			#print("i1", i1)
			#print("i2", i2)
			#print("operand", itm)

			if itm == '+':
				mstack.append(str(i1+i2))
			elif itm == '-':
				mstack.append(str(i1-i2))
			elif itm == '*':
				mstack.append(str(i1*i2))
			elif itm == '/':
				mstack.append(str(int(i1/i2)))
			#print("mstack", mstack)
			continue

		mstack.append(itm)
		#print("mstack", mstack)

	return int(float(mstack.pop()))

print(RPN(["2", "1", "+", "3", "*"]))
print(RPN(["4","13","5","/","+"]))
#print(RPN(["3", "4", "*", "5", "6", "*", "+"]))
#print(RPN(["3", "4", "-", "5", "+"]))
print(RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
