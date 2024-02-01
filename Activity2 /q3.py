def wordCount(t):
    """Returns a dictionary with words as keys and lists of line numbers as values."""
    word_dict = {}
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, 1):
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    word_dict[word].append(line_number)
                else:
                    word_dict[word] = [line_number]
    return word_dict

