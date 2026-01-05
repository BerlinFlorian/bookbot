import sys
from stats import get_num_words, get_letter_count, sort_letter_counts

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	num_words = get_num_words(book_text)
	num_letters = get_letter_count(book_text)
	sorted_list = sort_letter_counts(num_letters)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for i in range(len(sorted_list)):
		print(f"{sorted_list[i]["char"]}: {sorted_list[i]["num"]}")
	print("============= END ===============")


main()
