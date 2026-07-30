def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = get_book_text("books/frankenstein.txt")
    split = words.split()
    return len(split)

def main():
    num_words = word_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")

main()
