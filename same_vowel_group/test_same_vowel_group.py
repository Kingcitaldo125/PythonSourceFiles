from same_vowel_group import same_vowel_group

def test_same_vowel_group1():
	assert(same_vowel_group(["toe", "ocelot", "maniac"]) == ["toe", "ocelot"])
def test_same_vowel_group2():
	assert(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) == ["many"])
def test_same_vowel_group3():
	assert(same_vowel_group(["hoops", "chuff", "bot", "bottom"]) == ["hoops", "bot", "bottom"])
