import re
from requests import get

def main():
	url = "https://www.fairbornmunicipalcourt.us/"
	rgx = re.compile(r"marquee\">(.+)<\/div>.+<h2", re.MULTILINE | re.DOTALL)

	result = get(url)
	if result.status_code != 200:
		print("ERROR (curl)")
		return -1

	content = result.content.decode('utf-8')
	match = re.search(rgx,content)
	if match is None:
		print("ERROR (rgx)")
		return -1

	print(match.group(1))
	return 0

if __name__ == "__main__":
	main()
