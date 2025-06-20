def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import book_word_count
from stats import book_character_count

def main():
    path_to_file = "books/frankenstein.txt"
    wordcount = book_word_count(path_to_file)
    charcount = book_character_count(path_to_file)
    print(f"{wordcount} words found in the document")
    print(charcount)

if __name__ == "__main__":
    main()