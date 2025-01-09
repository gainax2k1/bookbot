# this was the official answer, but it doesn't work in vs code.
# I needed to add the import os, base path, path to file lines
#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    print(text)
#
#
#def get_book_text(path):
#    with open(path) as f:
#        return f.read()
#
#main()




def main():
    import os # magic code to make it work
    base_path = os.path.dirname(os.path.abspath(__file__)) # magic code to make it work
    path_to_file = os.path.join(base_path, 'books', 'frankenstein.txt')# magic code to make it work
    
    file_contents = get_book_text(path_to_file)
    word_count = wordcount(file_contents)
    character_dictionary = count_characters(file_contents)
    characters_sorted = make_sorted_dictionary(character_dictionary)

    #print("file contents:", file_contents)
    print(word_count, "words found in the document")
    #print("character counts:", character_dictionary)
    #print("characts_sorted:" , characters_sorted)

    for letters in characters_sorted:
        print(f"The '{letters['character']}' character was found {letters['num']} times")

def get_book_text(path_to_file): # this is all good
    with open(path_to_file) as f:
        return f.read()

def wordcount(file_contents): # this is all good
    words = file_contents.split() #splits "file_contents" into a LIST
    number_of_words = len(words) #len returns number of items in list
    return number_of_words

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
