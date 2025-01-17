# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    print(f"{num_words} words found in the document")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def wordcount(text):
    words = text.split()
    return len(words)