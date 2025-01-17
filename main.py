# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    chars_dict = charactercount(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def wordcount(text):
    words = text.split()
    return len(words)

def charactercount(text):
    characters = {}
    for c in text:
        low_characters = c.lower()
        if low_characters in characters:
            characters[low_characters] += 1
        else:
            characters[low_characters] = 1
    return characters


main()