def unique_letter(word):
    if not isinstance(word, str):
        return "ERROR"
    
    list1 = []

    for i in word:
        if i in list1:
            return False
        list1.append(i)

    return True


print(unique_letter("qwerty"))