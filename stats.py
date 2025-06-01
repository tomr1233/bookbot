def get_num_words(file):
    file_list = str.split(file)
    num = len(file_list)
    return num

def get_num_characters(book):
    book = book.lower()
    char_dict = {}
    for char in book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    sorted_list = []
    for i in char_dict:
        sorted_list.append({"char": i, "num": char_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list