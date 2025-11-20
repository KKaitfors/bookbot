from stats import count_book_words, count_book_characters, sort_characters
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    characters = count_book_characters(get_book_text(sys.argv[1]))
    book_path = sys.argv[1]
    num_words = count_book_words(get_book_text(book_path))
    character_report = sort_characters(characters) 

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for item in character_report:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

main()