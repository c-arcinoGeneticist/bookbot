def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = get_book_text("books/frankenstein.txt")
    split = words.split()
    return len(split)

def char_count(text):
    full_text = get_book_text(text)
    chars = {}

    for char in full_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars
