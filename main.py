from stats import word_count, char_count

def main():
    num_words = word_count("books/frankenstein.txt")
    how_many_chars = char_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")

    for char, times in how_many_chars.items():
        print(f"\'{char}\': {times}")

main()
