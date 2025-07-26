def count_word(txt): #counts words in txt
    words = txt.split()
    return len(words)

def count_characters(txt): #counts character in txt
    chars = txt.lower()
    char_counts = {}
    for char in chars:
        char_counts[char] = char_counts.get(char, 0) +1
    return char_counts

def sort_char_count(char_count): #removes non-alpha and sorts greatest to least
    sorted_chars = []
    for char, count in char_count.items():
       if char.isalpha():
        sorted_chars.append({"char" : char, "num": count})
    sorted_chars.sort(key=lambda item: item["num"], reverse = True)
    return sorted_chars
    



