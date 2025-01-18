# print("hello world")
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    chars_dict = charactercount(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    chars_dict_to_sorted_list(chars_dict)

    #print(f"{num_words} words found in the document")
    #print("Theser are the characters and numbers that are in the book.", chars_dict)

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

def sort_on(chars_dict):
    return chars_dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    x = None
    for i in chars_dict:
        print(f"The", i, "character was found", chars_dict[i], "times")

main()