from stats import sort_char_count

from stats import count_word

from stats import count_characters

def get_book_text(p): #converts file contents at path to a string
    with open(p) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    txt =get_book_text("./books/frankenstein.txt")
    num_count = count_word(txt)
    char_count = count_characters(txt)
    sorted_count = sort_char_count(char_count)
    report = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {} total words
--------- Character Count -------""".format(num_count)

    print(report)
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()