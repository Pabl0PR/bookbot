def count_words(txt):
    return len(txt.split())

def count_character(txt):

    character_dictionary = {}

    for letter in txt:
        if letter.lower() in character_dictionary:
            character_dictionary[letter.lower()] += 1
        else:
            character_dictionary[letter.lower()] = 1

    return character_dictionary

def dic_to_sorted_list(dic):

    def sort_on(dic):
        return dic['num']

    sorted_list = []

    for char in dic:
        sorted_list.append({"char": char, "num": dic[char]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
    
