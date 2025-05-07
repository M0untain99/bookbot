def count_words(words):
    all_words = words.split()
    return len(all_words)

def count_chars(words):

    char_dict = {}

    for char in words:

        character = char.lower()

        if character in char_dict.keys():
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict

def sort_on(dict):
    return dict['num']

def order_chars(chars):
    
    char_dicts = []

    for char in chars:
        temp_dict = {'char': char, 'num': chars[char]}
        char_dicts.append(temp_dict)

    char_dicts.sort(key=sort_on, reverse=True)

    return char_dicts