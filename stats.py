def get_num_words(book):
	return len(book.split())

def get_letter_count(book):
	dict = {}
	for l in book.lower():
		if l not in dict:
			dict[l] = 1
		else:
			dict[l] += 1
	return dict

def sort_on(items):
	return items["num"]

def sort_letter_counts(dict):
	"""Return a sorted list of letters and their counts ex: [{"char": "b", "num": 4868},{"char": "c", "num": 4768}]
	using .sort()"""

	liste = []
	for k,v in dict.items():
		liste.append({"char": k, "num": v})

	liste.sort(reverse=True, key=sort_on)

	return liste