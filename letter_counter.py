def letter_counter(word):
    if not isinstance(word, str):
        return "ERROR"
    
    dict1 = {}
    
    for i in word:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1       
    return dict1


print(letter_counter("afirmative"))