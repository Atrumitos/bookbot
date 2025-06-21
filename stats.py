def book_word_count(path_to_file):
    with open(path_to_file) as f:
        word_count = f.read().split()
        return len(word_count)

def book_character_count(path_to_file):
    with open(path_to_file) as f:
        wordcapped = f.read().split()
        words=[s.lower() for s in wordcapped]        
        characters=[char for word in words for char in word]
        characters_dict = {}
        for character in characters:
            if character in characters_dict:
                characters_dict[character] +=1 
            else:
                characters_dict[character] = 1
        return characters_dict

def characters_sorted(path_to_file):
    characters_dict = book_character_count(path_to_file)
    characters_dict_list = [{k: v} for k,v in sorted(characters_dict.items(), reverse=True, key=lambda item: item[1])]
    return characters_dict_list