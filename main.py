import sys

from stats import sort_char_count

from stats import count_word

from stats import count_characters

def get_book_text(p): #converts file contents at path to a string
    with open(p) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
    txt =get_book_text(book)
    num_count = count_word(txt)
    char_count = count_characters(txt)
    sorted_count = sort_char_count(char_count)
    report = (f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_count} total words
--------- Character Count -------""")

    print(report)
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()