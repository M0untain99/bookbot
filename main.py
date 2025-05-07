from stats import count_words, count_chars, order_chars

def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents


def __main__():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    chars = count_chars(text)
    ordered = order_chars(chars)

    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')

    for char in ordered:
        if char['char'].isalpha():
            print(f'{char['char']}: {char['num']}')

    print('============= END ===============')

__main__()