from stats import count_words, count_characters

def print_report(file, word_count, char_counts):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document\n\n")
    for char, count in char_counts.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times\n")
    print(f"--- End report ---")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_characters(file_contents)
        print_report("books/frankenstein.txt", word_count, char_counts)
        

if __name__ == "__main__":
    main()