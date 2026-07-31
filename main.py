from stats import word_count, char_count, chars_dict_to_sorted_list

def main():
    num_words = word_count("books/frankenstein.txt")
    how_many_chars = char_count("books/frankenstein.txt")
    characters_counted = chars_dict_to_sorted_list(how_many_chars)
    print_report("books/frankenstein.txt", num_words, characters_counted)

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
main()
