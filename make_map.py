import random

def ran_bit():
	rb = random.randrange(0,3)
	return 1 if rb == 1 else 0

def make_map(rows, cols):
	return [[ran_bit() for j in range(cols)] for i in range(rows)]

def format(mmap, rows, cols):
	s_string = f"\tstd::array<std::array<char,{cols}>,{rows}>"
	s_string += " grid{"
	s_string += "\n"
	for row in mmap:
		s_string += "\t\t"
		s_string += f"std::array<char,{cols}>"
		s_string += "{"
		for r in range(len(row)-1):
			s_string += "'"
			s_string += str(row[r])
			s_string += "'"
			s_string += ", "
		s_string += "'"
		s_string += str(row[-1])
		s_string += "'"
		s_string += "},"
		s_string += "\n"

	s_string += "\t};"
	return s_string


rows = 8
cols = 8

if __name__ == "__main__":
	arr_syntx = format(make_map(rows, cols), rows, cols)

	with open('out.cpp', 'w') as f:
		f.write(arr_syntx)
		f.write("\n")
		f.flush()
