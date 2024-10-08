def reverse_word(word):
    if not isinstance(word, str):
        return "ERROR"
    
    list1 =[]

    right = len(word) - 1
    while 0 <= right:  
        list1.append(word[right])
        x = "".join(list1)
        right -= 1
    return x
    
print(reverse_word("levani"))