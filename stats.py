def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_char_count_dict(text):
    word_car = text.lower()
    char_dict = {}

    for char in word_car:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    sort_list = []
    for key in char_dict:
        if key.isalpha():
            sort_list.append({"name": key, "num": char_dict[key]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list