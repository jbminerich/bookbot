def word_count(book_text):
    split_words = book_text.split()
    num_words = 0
    for word in split_words:
        num_words += 1
    return num_words

def char_count(book_text):
    chars={}
    low_text = book_text.lower()

    for char in low_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_dict(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=lambda d: d["count"], reverse=True)
    return sorted_list