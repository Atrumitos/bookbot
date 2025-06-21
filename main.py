import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import book_word_count
from stats import book_character_count
from stats import characters_sorted

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path_to_file = sys.argv[1]
    wordcount = book_word_count(path_to_file)
    charcount = characters_sorted(path_to_file)
    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_file}...
----------- Word Count ----------
Found {wordcount} total words
--------- Character Count -------"""
    )
    for d in charcount:
        for char, count in d.items():
            if char.isalpha():        
                print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()