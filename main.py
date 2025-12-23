import sys

from stats import count_letters_sorted, count_words


def main():
    path = process_args()
    txt = get_book_text(path)
    num_words = count_words(txt)

    reports = count_letters_sorted(txt)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for report in reports:
        print(f"{report["char"]}: {report["num"]}")

    print("============= END ===============")


def process_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return sys.argv[1]


def get_book_text(path):
    with open(path) as book:
        return book.read()



main()
