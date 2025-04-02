from stats import word_count, char_count, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with the file
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    the_text = get_book_text(sys.argv[1])
    num_words = word_count(the_text)
    characters = char_count(the_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars =  sort_dict(characters)
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
main()

