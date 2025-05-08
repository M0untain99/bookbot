from stats import count_words, count_chars, order_chars
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents


def __main__():
    if len(sys.argv) != 2:  # If there are not 2 command arguments
        print(f'Usage: python3 main.py <path_to_book>')  # Explain how to use tool
        sys.exit(1)  # Exit the program with error code 1

    text = get_book_text(sys.argv[1])  # Send the book file entered by the user as a command argument
    num_words = count_words(text)  # Count the number of words
    chars = count_chars(text)  # Count how many time each character appears
    ordered = order_chars(chars)  # Order the characters by frequency

    print(f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')

    for char in ordered:
        if char['char'].isalpha():
            print(f'{char['char']}: {char['num']}')

    print('============= END ===============')

__main__()