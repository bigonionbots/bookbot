def main():
    generate_report("books/frankenstein.txt")


def generate_report(book):
    book_text = get_book_text(book)
    num_words = word_count(book_text)
    letters = letter_count(book_text)

    sorted = sorted_letters(letters)
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    for s in sorted:
        print(f"The '{s['letter']}'character was found {s['count']} times")

    print("--- End report ---")


def sort_on(d):
    return d["count"]


def sorted_letters(counted):
    sorted = []
    for letter in counted:
        sorted.append({"letter": letter, "count": counted[letter]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def word_count(str):
    words = str.split()
    return len(words)


def letter_count(s):
    str = s.lower()
    letters = {}
    for i in range(0, len(str)):
        if str[i].isalpha() == True:
            try:
                letters[str[i]] += 1
            except Exception:
                letters[str[i]] = 1
    return letters


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()
