def get_num_words(file):
    with open(file, "r", encoding="utf-8") as f:
        book_text = f.read()
    words = book_text.split()
    counter = len(words)
    return f"Found {counter} total words"

def get_character_count(file):
    characters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "æ": 0, "â": 0, "ê": 0, "ë": 0, "ô": 0}
    with open(file, "r", encoding="utf-8") as f:
        book_text = f.read()
    words = book_text.split()
    for i in words:
        lower = i.lower()
        for j in lower:
            if j in characters:
                characters[j] += 1
            else: continue
    return characters

def sorted_list(file):
    characters = get_character_count(file)

    sorted_chars = sorted(
        characters.items(),
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_chars