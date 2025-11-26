import sys
from stats import sorted_list, get_num_words

try:
    sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(relative_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(get_num_words(relative_path))
    print("--------- Character Count -------")
    for key, value in sorted_list(relative_path):
        print(f"{key}: {value}")
    return "============= END ==============="

print(main(sys.argv[1]))