from stats import get_number_of_words, get_char_count_dict, sort_char_dict
from sys import argv, exit

def get_books_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)
    path_to_file = argv[1]
    books_text = get_books_text(path_to_file)
    num_words = get_number_of_words(books_text)
    char_count_dict = get_char_count_dict(books_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in (sort_char_dict(char_count_dict)):
        print(f"{item['name']}: {item['num']}")
    print("============= END ===============")
main()