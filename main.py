from stats import count_words, count_characters
import sys

def print_report(file, word_count, char_counts):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document\n\n")
    for char, count in char_counts.items():
        if char.isalpha():
            print(f"{char}: {count}\n")
    print(f"--- End report ---")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_characters(file_contents)
        print_report(sys.argv[1], word_count, char_counts)
        

if __name__ == "__main__":
    main()