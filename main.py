import sys
from stats import count_words, count_character, dic_to_sorted_list

def get_book_text(filePath):
    book_text = ""
    with open(filePath) as f:
        book_text = f.read()
    return book_text

def printReport(bookPath, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    book_word_count = count_words(book_text)

    book_character_count = count_character(book_text)
    #print(book_character_count)

    printReport(book_path, book_word_count)
    result = dic_to_sorted_list(book_character_count)
    for element in result:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

    print("============= END ===============")


main()



        