def get_book_text(book):
	with open(book) as f:
		return f.read()

def get_num_words(bookpath):
	num_words = 0
	words = get_book_text(bookpath).split()
	for word in words:
		num_words += 1
	print(f"Found {num_words} total words")

#takes the characters in a .txt and adds them to a dictionary with the key being each character storing how many times it occured. Returns 1 Dictionary
def get_num_char(bookpath):
    char_count = {}
    book = get_book_text(bookpath)
    for char in book:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return sorted_dict(char_count)

#takes a dictionary of characters and their count and returns a sorted list of dictionaries
def sorted_dict(char_count):
    char_list = []
    for char, count in char_count.items():
          char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

#helper sort function
def sort_on(item):
      return item["num"]

def report(bookpath):
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {bookpath}")
      get_num_words(bookpath)
      print("--------- Character Count -------")
      for dictionary in get_num_char(bookpath):
            if dictionary["char"].isalpha():
                print(f"{dictionary["char"]}: {dictionary["num"]}")
