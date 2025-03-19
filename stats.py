def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()  # convert to lowercase
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def count_words(text):
    words = text.split()
    return len(words)