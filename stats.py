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