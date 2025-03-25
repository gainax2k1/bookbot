def wordcount(file_contents): # this is all good
    words = file_contents.split() #splits "file_contents" into a LIST
    number_of_words = len(words) #len returns number of items in list
    return number_of_words