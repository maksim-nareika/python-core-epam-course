def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    words = s.split(" ")
    ordered_words = []

    for word in words:
        # first_word = ordered_words[0] if len(ordered_words) > 0 else word
        if len(ordered_words) == 0:
            ordered_words.append(word)
            continue
        if len(ordered_words[0]) < len(word):
            ordered_words.insert(0, word)
        elif len(ordered_words[0]) == len(word):
            ordered_words.insert(1, word)
        else:
            ordered_words.append(word)

    return ordered_words[0]
