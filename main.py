
def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text)
    print(word_count)

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()