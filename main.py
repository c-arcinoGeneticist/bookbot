from stats import get_book_text, word_count, char_count, chars_dict_to_sorted_list
import sys

def main():
    check_for_two()
    path_to_text = get_book_text(sys.argv[1])
    num_words = word_count(path_to_text)
    how_many_chars = char_count(path_to_text)
    characters_counted = chars_dict_to_sorted_list(how_many_chars)
    print_report(sys.argv[1], num_words, characters_counted)

def print_report(book_path, num_words, sorted_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for pair in sorted_list:
            if pair[0].isalpha():
                print(f"{pair[0]}: {pair[1]}")
        print("============= END ===============")

def check_for_two():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
