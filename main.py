def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def get_num_words(book):
	return len(book.split())

def main():
	num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
	print(f"Found {num_words} total words")

main()
