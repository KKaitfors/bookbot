# Returns the number of words in the provided text
def count_book_words(text):
    word_count = len(text.split())
    return word_count

# Returns a dictionary of lowercase characters with the character as the key and its number of appearances in the text as the value
def count_book_characters(text):
    character_count = {}
    for character in text:
        lowered = character.lower()
        if lowered not in character_count:
            character_count[f"{lowered}"] = 1
        else:
            character_count[f"{lowered}"] += 1
    return character_count

# Helper function for sorting in sort_characters()
def sort_on(items):
        return items["num"]

# Takes a dictionary and returns a list of dictionaries with the entries sorted from largest to smallest
def sort_characters(dictionary):
    sorted_list = []
    for char in dictionary:
        sorted_list.append({"char": char, "num": dictionary[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

