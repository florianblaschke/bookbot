def count_words(txt):
    words = txt.split()
    return len(words)

def count_letters(txt):
    letter_map = {}
    for letter in list(txt):
        lower_case = letter.lower()

        if not lower_case.isalpha():
            continue

        if lower_case in letter_map:
            letter_map[lower_case] += 1
        else:
            letter_map[lower_case] = 1

    return letter_map

def sort_on(items):
    return items["num"]

def count_letters_sorted(txt):
    chars = count_letters(txt)
    structured = []

    for char in chars:
        struct = {"char": char, "num": chars[char]}
        structured.append(struct)

    structured.sort(reverse=True,key=sort_on)

    return structured
