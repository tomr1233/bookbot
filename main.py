from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    result = get_book_text(file_path)
    num_words = get_num_words(result)
    num_characters_dict = get_num_characters(result)
    sorted_dict = sort_dict(num_characters_dict)

    print(
        f"""============ BOOKBOT ============
Analyzing book found at {file_path}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
    )
    for i in sorted_dict:
        if i['char'].isalpha() == True:
            print(f"{i['char']}: {i['num']}")
        else:
            pass
    print("============= END ===============")
main()