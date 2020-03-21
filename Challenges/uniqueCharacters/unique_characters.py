def unique_characters(word):
    visited_chars = set()

    for i in range(len(word)):
        letter = word[i]

        if letter in visited_chars:
            return False
        
        visited_chars.add(letter)
    
    return True

print(unique_characters("abc"))
print(unique_characters(""))
print(unique_characters("aabc"))