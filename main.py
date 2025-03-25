from stats import wordcount

def main():
    import os # magic code to make it work
    import sys # to allow sys.argv functionality

    base_path = os.path.dirname(os.path.abspath(__file__)) # magic code to make it work
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]


    # old way: path_to_file = os.path.join(base_path, 'books', 'frankenstein.txt')# magic code to make it work
    
    file_contents = get_book_text(path_to_file)
    word_count = wordcount(file_contents)
    character_dictionary = count_characters(file_contents)
    characters_sorted = make_sorted_dictionary(character_dictionary)

    #print("file contents:", file_contents)
    print(word_count, "words found in the document")
    #print("character counts:", character_dictionary)
    #print("characts_sorted:" , characters_sorted)

    for letters in characters_sorted:
        # old way: print(f"The '{letters['character']}' character was found {letters['num']} times")
        print(f"{letters['character']}: {letters['num']}")
    
def get_book_text(path_to_file): # this is all good
    with open(path_to_file) as f:
        return f.read()



def count_characters(file_contents): # good? same as "get chars dict"
    character_counts = {}

    for letters in file_contents:
        lowered_string = letters.lower()
        if lowered_string.isalpha(): # ensures only letters counted in dictionary
            if lowered_string in character_counts:
                character_counts[lowered_string] += 1
            else:
                character_counts[lowered_string] = 1
    return character_counts

def make_sorted_dictionary(character_counts): 
    proper_dictionary = []
    for entries in character_counts:
        proper_dictionary.append({"character": entries, "num":character_counts[entries]})
    proper_dictionary.sort(reverse=True, key=sort_on)
    return proper_dictionary

def sort_on(dict): #not sure what does?
    #print("sort_on called")
    return dict["num"]
    
main()
