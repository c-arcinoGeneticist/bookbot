def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return len(words)

def char_count(text):
    chars = {}

    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(sorted: tuple[str, int]) -> int:
        return sorted[1]

def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []

    for char in chars:
        char_value = chars[char]
        char_tuple = (char, char_value)
        sorted_list.append(char_tuple)

    descending_sorted_list = sorted(sorted_list, reverse=True, key=sort_on)

    return descending_sorted_list
