from stats import word_count

def main():
    num_words = word_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")

main()
