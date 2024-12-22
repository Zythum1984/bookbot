def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)
        sorted_char_count = sort_dict(char_count)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        for item in sorted_char_count:
            print(f"The \"{item['char']}\" character was found {item['count']} times")
        print("--- End report ---")

def count_words(file_contents):
    words_in_string = file_contents.split()
    word_count = len(words_in_string)
    return word_count

def count_chars(file_contents):
    sanitized = file_contents.lower()    
    char_list = list(sanitized)
    char_dict = {}
    for char in char_list:
        if(char not in char_dict):
            char_dict.update({char: 1})
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict(dict):
    dict_list = []
    for key, value in dict.items():
        if key.isalpha():
            dict_list.append({"char": key, "count": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["count"]

main()