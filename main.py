from stats import word_count, char_count, chars_dict_to_sorted_list

def main():
    num_words = word_count("books/frankenstein.txt")
    how_many_chars = char_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")

    characters_counted = chars_dict_to_sorted_list(how_many_chars)
    print(characters_counted)
main()
