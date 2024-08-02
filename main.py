def count_words(book):
    words = book.split()
    return len(words)

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
        print(count_words(file_contents))
def count_characters(book):
    lowbook = book.lower()
    letters={}
    for char in lowbook:
        if(char in letters):
            letters[char]+=1
        else:
            if(char.isalpha()):
                letters[char] = 1
    return letters

def sort_letters(letters):
    items = list(letters.items())
    items.sort(reverse = True)
    return letters

def print_occurence(letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(get_book_text())} words found in the document")
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")


def main():
    book= get_book_text()
    print_occurence(sort_letters(count_characters(book)))

main()
