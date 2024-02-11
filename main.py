
def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text)
    letters = letter_count(text)
    letters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for sorted_letter in letters:
        print(f"The {sorted_letter["letter"]} was found {sorted_letter["count"]} times")
    print("--- End report ---")
    

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters_with_count = {}
    for character in text:
        lower = character.lower()
        if lower.isalpha():
            if lower not in letters_with_count:
                letters_with_count[lower] = 1
            else:
                letters_with_count[lower] += 1

    letters_with_count_list = []
    for letter in letters_with_count:
        letter_with_count = { "letter": letter, "count": letters_with_count[letter]}
        letters_with_count_list.append(letter_with_count)

    return letters_with_count_list

def sort_on(dict):
    return dict["count"]

main()