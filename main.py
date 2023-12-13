def get_char_counts(words):
    counts = {}
    
    for word in words:
        for char in word:
            c = char.lower()
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

    return counts

def generate_report(char_counts):
    lst = [ (k, v) for k, v in char_counts.items()]
    letter_counts = list(filter(lambda x: x[0].isalpha(), lst))
    letter_counts.sort(key=lambda x: x[1], reverse=True)
    return letter_counts

def main():
    book_path = 'books/frankenstein.txt'
    
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.split()

        char_counts = get_char_counts(words)

        letter_counts = generate_report(char_counts)

        print(f"--- Begin report of {book_path} ---")
        print(f"{len(words)} words found in the document\n")
        for pair in letter_counts:
            print(f"The '{pair[0]} character  was found {pair[1]} times'")
        print("\n--- End report ---")


main()
